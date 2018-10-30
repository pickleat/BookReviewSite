import os
# import requests
from flask import Flask, session, render_template, request, redirect, url_for, escape
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from rauth.service import OAuth1Service, OAuth1Session

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


# # Get a real consumer key & secret from: https://www.goodreads.com/api/keys
# CONSUMER_KEY = 'B5C9TI2uE44xXNV76cDg'
# CONSUMER_SECRET = 'abXw3Ondy6TVDVdpe1qrObnjIm3wzDWeh0EMyzAWGM'

# goodreads = OAuth1Service(
#     consumer_key=CONSUMER_KEY,
#     consumer_secret=CONSUMER_SECRET,
#     name='goodreads',
#     request_token_url='https://www.goodreads.com/oauth/request_token',
#     authorize_url='https://www.goodreads.com/oauth/authorize',
#     access_token_url='https://www.goodreads.com/oauth/access_token',
#     base_url='https://www.goodreads.com/'
#     )

# # head_auth=True is important here; this doesn't work with oauth2 for some reason
# request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

# authorize_url = goodreads.get_authorize_url(request_token)
# print('Visit this URL in your browser: ' + authorize_url)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))