# Import packages to connect to PostgreSQL database
import os
import psycopg2
from psycopg2 import sql

# Connect to the database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

# Allow database creation
conn.autocommit = True

# Create a cursor/pointer
cur = conn.cursor()

# Check if the database already exists
cur.execute(
    "SELECT 1 FROM pg_database WHERE dataname = %s;",
    ("tvshow",)
)

# Create database if it does not exist
if cur.fetchone() is None:
    cur.execute(
        sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier("tvshow")
        )
    )
    print("Database created successfully!")
else:
    print("Database already exists!")

# Close cursor and connection
cur.close()
conn.close()

# Connect to the database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

# Create a cursor/pointer
cur = conn.cursor()

# Create users table
sql = """
CREATE TABLE IF NOT EXISTS users (
    userid VARCHAR(50) NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(200) NOT NULL,
    account_type VARCHAR(40) NOT NULL
);
"""
cur.execute(sql)

# Create TV Shows table
sql = """
CREATE TABLE IF NOT EXISTS tv_shows (
    show_id VARCHAR(50) NOT NULL PRIMARY KEY,
    genre VARCHAR(50),
    title VARCHAR(50),
    release_date DATE,
    seasons INTEGER,
    episodes INTEGER,
    rating FLOAT,
    cast_member VARCHAR(50),
    premium_info BOOLEAN
);
"""
cur.execute(sql)

# Create Payments table
sql = """
CREATE TABLE IF NOT EXISTS payments (
    payment_id VARCHAR(50) NOT NULL PRIMARY KEY,
    user_id VARCHAR(50),
    show_id VARCHAR(50),
    amount DECIMAL(10,2),
    payment_date DATE,
    payment_status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(userid),
    FOREIGN KEY (show_id) REFERENCES tv_shows(show_id)
);
"""
cur.execute(sql)

# Commit the SQL code to the database
conn.commit()

# Close the cursor object
cur.close()

# Close the database connection
conn.close()

print("Database tables created successfully!")
