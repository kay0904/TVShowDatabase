#import render_template function and redirect functions from flask
from flask import render_template, redirect, session, flash, request, url_for
#import app variable from app package
from app import app
#import LoginForm class from out forms.py file
from app.forms import LoginForm
from app.forms import RegisterForm
#import psycopg2 to connect to database
import psycopg2
import os
#import encryption to hash passwords and compare during user login
from werkzeug.security import check_password_hash

#create an assocation for the URL /
@app.route('/')

#Create the index page to display intro text
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
      
#Create the About us page to display intro text
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title='About Us')
   
#create an assocation for search   
@app.route('/search')
def search():
    # Get the title and genre entered by the user
    search_title = request.args.get('search', '')
    genre = request.args.get('genre', '')
    
    # Create the database connection
    def db_connect():
        return psycopg2.connect(
            database="tvshow",
            user="postgres",
            password=os.environ["DB_PASSWORD"],
            host="localhost",
            port="5432"
        )
    # Connect to PostgreSQL
    conn = db_connect()

    cur = conn.cursor()

    # Search for matching TV shows
    sql = """SELECT title, genre, release_date, seasons,
                    episodes, rating, cast_member, premium_info
             FROM tv_shows
             WHERE title ILIKE %s"""

    params = ['%' + search_title + '%']

    # Filter by genre if selected
    if genre:
        sql += " AND genre = %s"
        params.append(genre)

    # Execute query and retrieve results
    cur.execute(sql, params)
    shows = cur.fetchall()

    # Close connection
    cur.close()
    conn.close()

    # Display search results
    return render_template('search.html', title = 'Search', shows=shows)

#create an assocation for add show     
@app.route('/addtvshow')
def add_show():
    return render_template('add_show.html', title='Add TV Show')

#create an assocation for add show     
@app.route('/payment')
def payment():
    return render_template('payment.html', title='Payment')
    
#create an assocaiton for register  
@app.route('/register', methods=['GET', 'POST'])  
def register():
    form = RegisterForm()
   
    if form.validate_on_submit():
        return redirect('/index')
   
    return render_template('register.html', title="Sign up", form = form)

#create an assocaiton for the URL /login
@app.route('/login', methods=['GET', 'POST'])
#create the login page to display web form for user
def login():
    #create an instance of a loginform and store in a variable called form
    form = LoginForm()
         
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        conn = db_connect()
        cur = conn.cursor()

        sql = "SELECT password FROM users WHERE userid = %s;"
        cur.execute(sql, (username,))

        user_data = cur.fetchone()

        cur.close()
        conn.close()

        if user_data and check_password_hash(user_data[0], password):
            session["user_id"] = username
            flash("Logged in successfully!")
            return redirect('/index')
        else:
            flash("Invalid username or password.")
   
    return render_template('login.html', title="Sign In", form = form)
    
   #create an assocation for logout 
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("index"))
    
    
#create the database connection
def db_connect():
    return psycopg2.connect(
        database="tvshow",
        user="postgres",
        password=os.environ["DB_PASSWORD"],
        host="localhost",
        port="5432"
    )l', title="Sign up", form = form)
