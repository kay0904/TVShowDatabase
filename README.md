# TVShowDatabase
## Project Description
TV Show Database is a web application developed using
Python, Flask and PostgreSQL. The application allows
users to explore information about different TV shows.

This project was developed for the INFO8021
DevOps Strategy and Automation module.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- PostgreSQL
- pgAdmin 4
- GitHub

## Website Pages
- **Home:** Introduces the application and its features.
- **About Us:** Provides information about the application.

## Database
The PostgreSQL database contains three tables:

- **Users:** Stores user account information.
- **TV_Shows:** Stores TV show information.
- **Payments:** Stores payment records.

## Project Files
- `routes.py` - Flask application routes.
- `__init__.py` - Initialises the Flask application.
- `config.py` - Application configuration.
- `initialise_db.py` - Creates the database and tables.
- `populate_db.py` - Inserts database records.
- `requirements.txt` - Required Python packages.

## Installation
1. Clone or download the repository.
2. Install the required packages:
   `pip install -r requirements.txt`
3. Configure PostgreSQL and environment variables.
4. Run `python initialise_db.py`
5. Run `python populate_db.py`
6. Start the Flask application.

## Future Development
Future features will include:
- User Registration
- User Login and Logout
- Search TV Shows
- View TV Show Information
- Payment Options
- Statistics and Graphs
