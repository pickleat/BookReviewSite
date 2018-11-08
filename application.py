import os
import requests
from flask import Flask, session, render_template, request, redirect, url_for, escape, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from rauth.service import OAuth1Service, OAuth1Session
import json
app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# Get a real consumer key & secret from: https://www.goodreads.com/api/keys
CONSUMER_KEY = 'zpujku3fRCT0dBhaSF4lA'
CONSUMER_SECRET = 'BYbhjlnYBrZ5GoNxwryF7u6KMdDJMt2pvV4f0xaQ5g'

goodreads = OAuth1Service(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    name='goodreads',
    request_token_url='https://www.goodreads.com/oauth/request_token',
    authorize_url='https://www.goodreads.com/oauth/authorize',
    access_token_url='https://www.goodreads.com/oauth/access_token',
    base_url='https://www.goodreads.com/'
    )

# head_auth=True is important here; this doesn't work with oauth2 for some reason
request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

authorize_url = goodreads.get_authorize_url(request_token)
# print('Visit this URL in your browser: ' + authorize_url)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['search'] = request.form['search']
        session['column'] = request.form['column']
        return redirect(url_for('results'))
    # return render_template('index.html') #redirect(url_for('results'))
    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        auth = db.execute("SELECT * FROM users where username = '" + user + "' AND password = '" + password + "'")
        for item in auth:
            if str(item[0]) == user and str(item[1]) == password:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        else:
            flash('username and/or password does not match')
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('logout.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try: 
            db.execute('INSERT INTO users (username, password) VALUES (:username, :password)',
            {'username': username, 'password': password})
            db.commit()        
        except:
            flash('username taken, try another, or if this is your username, go to the sign in page')
            return redirect(url_for('register'))
        flash("You've successfully registered")
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/results')
def results():
    """Lists queried items"""
    query = db.execute("Select * from books where " + session['column'] + " ilike '%" + session['search'] + "%'").fetchall()
    return render_template('results.html', query=query)

@app.route('/<isbn_variable>', methods=['Get', 'POST'])
def book(isbn_variable):
    """Creates a Book page for a specific book by ISBN"""
    book = db.execute("Select * from books where isbn = '" + isbn_variable + "'").fetchall()
    data = {"format":"json", "user_id": "25884519", "isbn":isbn_variable}
    goodreadsreviews = requests.get("https://www.goodreads.com/book/isbn/" + isbn_variable + "?key=" + CONSUMER_KEY, data)
    
    # this is "working, but still isn't formatted correctly"
    print(goodreadsreviews.status_code)
    passit = goodreadsreviews.json()
    for key in passit:
        if key == "reviews_widget":
            stuff = passit['reviews_widget']
            # print(stuff)
    reviews = db.execute("Select * from reviews where isbn = '" + isbn_variable + "'").fetchall()
    if request.method == 'POST':
        user = session['username']
        stars = request.form['stars']
        review = request.form['review']
        try:
            db.execute('INSERT into reviews (username, isbn, stars, review) VALUES (:username, :isbn, :stars, :review)',
            {"username": user, "isbn": isbn_variable, "stars": stars, "review": review})
            db.commit()
            flash('Review Submitted')
        except:
            flash("You've already submitted a review for this book")
            # return render_template('result.html', book=book)  
        return render_template('result.html', book=book, reviews=reviews, stuff=stuff)
    
    return render_template('result.html', book=book, reviews=reviews, stuff=stuff)

# @app.route('/api/<isbn_variable>')
# def goodreads(isbn_variable):
#     """Calls the Goodreads API and displays a JSON with """