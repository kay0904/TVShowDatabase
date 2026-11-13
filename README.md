# TVShowDatabase

## Project Description
TV Show Database is a web application developed using
Python, Flask and PostgreSQL. The application allows
users to explore information about different TV shows.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Jinja2
- PostgreSQL
- pgAdmin 4
- GitHub

## Website Pages
- **Home:** Introduces the application and its features.
- **About Us:** Provides information about the application.
- **Search TV Shows:** Allows users to search for TV shows
  by title or genre using records from PostgreSQL.
- **Login:** Allows registered users to log in.
- **Register:** Provides a user registration form.
- **Add TV Show:** Provides a page for adding TV shows.
- **Payments:** Provides a page for payment functionality.

## Database
The PostgreSQL database contains three tables:

- **Users:** Stores user account information.
- **TV_Shows:** Stores TV show information, including
  title, genre, release date, seasons, episodes and rating.
- **Payments:** Stores payment records.

## Project Files
- `routes.py` - Flask application routes.
- `__init__.py` - Initialises the Flask application.
- `config.py` - Application configuration.
- `initialise_db.py` - Creates the database and tables.
- `populate_db.py` - Inserts database records.
- `requirements.txt` - Required Python packages.
- `README.md` - Project information and instructions.

## Installation
## Installation

1. Clone or download the repository.

2. Install Python and PostgreSQL.

3. Install the required packages:

   `pip install -r requirements.txt`

4. Configure PostgreSQL and set the DB_PASSWORD environment variable.

   The application requires a PostgreSQL password to connect
   to the database. Use the password for your local PostgreSQL
   user rather than the original developer's password.

   For Windows Command Prompt:

   `set "DB_PASSWORD=your_postgresql_password"`

   For PowerShell:

   `$env:DB_PASSWORD = "your_postgresql_password"`

   Replace `your_postgresql_password` with your own
   PostgreSQL password.

5. Create the database and tables:

   `python initialise_db.py`

6. Populate the database:

   `python populate_db.py`

7. Start the Flask application in the same terminal:

   `python -m flask run`

8. Open the local website address displayed in the terminal.
## Project Status
The project is currently under development.

The Home and About Us pages have been created.
The Search TV Shows functionality has been connected
to PostgreSQL, allowing users to search for TV shows
by title or genre and the Login/Register functionality 
has been created.

Additional database functionalities are being
developed and tested.

## Future Development
Future development will focus on:
- Saving new user registrations to PostgreSQL.
- Adding TV shows through the website.
- Implementing payment functionality.
- Improving website design and functionality.

## Developer
Developed for the INFO8021 DevOps Strategy
and Automation module at Munster Technological
University (MTU).
