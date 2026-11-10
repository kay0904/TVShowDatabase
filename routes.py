#import render_template function and redirect functions from flask
from flask import render_template, redirect
#import app variable from app package
from app import app
#import LoginForm class from out forms.py file
from app.forms import LoginForm
from app.forms import RegisterForm

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
    
@app.route('/search')
def search():
    return render_template('search.html')

#create an assocaiton for the URL /login
@app.route('/login', methods=['GET', 'POST'])
#create the login page to display web form for user
def login():
    #create an instance of a loginform obj and store in a variable called form
    form = LoginForm()
   
    if form.validate_on_submit():
        return redirect('/index')
   
    return render_template('login.html', title="Sign In", form = form)
    
@app.route('/register', methods=['GET', 'POST'])  
def register():
    form = RegisterForm()
   
    if form.validate_on_submit():
        return redirect('/index')
   
    return render_template('register.html', title="Sign up", form = form)