# Project 1

Web Programming with Python and JavaScript

# Objectives:
Over the course of this assignment I spent many hours reading and researching the documentation around Flask, Jinja2, PostgreSQL, Heroku, and HTML/CSS. It has taught me a lot about HOW to look for help and answers. This project has given me so much confidence that with enough time and energy I can create dynamic sites with Flask/Jinja2/Python.

# Todos:
**Login/Out/Registration Functionality**
> Registration: Users should be able to register for your website, providing (at minimum) a username and password.
- [x] Registration - check if username is taken or not.
- [x] Users are able to create a simple username and password (added a disclaimer that this site is not about security, so don't use a real password)
> Login: Users, once registered, should be able to log in to your website with their username and password.
- [x] Not logged in redirect to login/registration page
- [x] Initial Login/ needs better functionality. 
- [x] Login Database: created user database, but probably not in its complete form. Just a simple username/password/id setup currently. 
> Logout: Logged in users should be able to log out of the site.
- [x] Users are able to logout with one click on any page

**Import Books.csv**
> Import: Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN nubmer, a title, an author, and a publication year. In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database. You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another. Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code.
- [x] Import.py finished. 
    - [x] Figure out how to skip the initial header lines. 
    - [x] ISBN's are treated as strings because of "x" found in many ISBNs.

**Search**
> Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
- [x] Search via ISBN/Title/Author, should dynamically respond with appropriate title(s) 
    - [x] Used '%' for the before and after as well 
    - [x] Also used 'ilike' but it doesn't perfectly return all searched results. 

**Book Page**
> Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
- [x] Dynamically return page based on book's ISBN. 
- [x] Pull all and display user avg review and number of reviews from Goodreads API.
- [x] Display all previous reviews submitted through my site. 
- [x] Add review form. 

**Review Submission**
> Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
- [x] Create Review Submission Database, it should:
    - [x] Allow a user to submit a review but only ONE. 

**GoodReads API Integration**
>Goodreads Review Data: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.
>API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:
"""{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}"""
> If the requested ISBN number isn’t in your database, your website should return a 404 error.
- [x] above works!


**Other Info**

I used a **create.sql** page (as shown in the lecture) to document how the database tables were created and relate to each other.

Originally the HTML/CSS formatting was done with Bootstrap, but I found it to be buggy and not as flexible as I would like. So I implemented my own custom CSS with Sass and .scss file which gave more customization and a better look and feel.