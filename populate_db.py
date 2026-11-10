# Import packages to allow opening a CSV file and connection to PostgreSQL database
import os
import psycopg2
import csv
from werkzeug.security import generate_password_hash

# Connect to the database
conn = psycopg2.connect(
    database="tvshow",
    user="postgres",
    password="postgress",
    host="localhost",
    port="5432"
)

# Create a cursor/pointer
cur = conn.cursor()

# Store the path of the user CSV file
path = "./data/"
csv_file_users = path + "users.csv"
csv_file_tvshows = path + "tvshow.csv"
csv_file_payments = path + "payments.csv"

# Counter to create a primary key with incrementing number
counter = 1

# Open user data file and read in data row by row to insert into table users
with open(csv_file_users, newline="") as csvfile:
    dataReader = csv.reader(csvfile, delimiter=",")

    for row in dataReader:
        # Hash the user's password
        pk = "u" + str(counter)
        counter += 1
        hashed_password = generate_password_hash(row[2])

        # Create SQL code to insert values into users table
        sql = "INSERT INTO users(userid, username, email, password, account_type) VALUES ('"+pk+"','"+row[0]+"','"+row[1]+"','"+generate_password_hash(row[2])+"','"+row[3]+"');"
        # Execute the SQL code
        cur.execute(sql, (pk, row[0], row[1], hashed_password, row[3]))

counter = 1
# Open data file and read in data row by row to insert into table tv shows
with open(csv_file_tvshows, newline="") as csvfile:
    dataReader = csv.reader(csvfile, delimiter=",")

    for row in dataReader:
        # Create a unique primary key
        pk = "s" + str(counter)
        counter += 1

        # Create SQL code to insert values into the table tv shows
        sql = "Insert into tv_shows(show_id, genre, title, release_date,seasons, episodes, rating, cast_member,premium_info) values ('"+pk+"','"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+","+row[4]+","+row[5]+",'"+row[6]+"',"+row[7]+");"
   
        # Execute the SQL code
        cur.execute(sql, (
            pk, row[0], row[1], row[2], row[3],
            row[4], row[5], row[6], row[7].strip().lower() == "true"
            
        ))
        
counter = 1 
# Open data file and read in data row by row to insert into table payments
with open(csv_file_payments, newline="") as csvfile:
    dataReader = csv.reader(csvfile, delimiter=",")

    for row in dataReader:
        # Create a unique primary key
        pk = "p" + str(counter)
        counter += 1

        # Create SQL code to insert values into the table payments
        sql = "Insert into payments (payment_id, user_id, show_id,amount, payment_date, payment_status) values ('"+pk+"','"+row[0]+"','"+row[1]+"',"+row[2]+",'"+row[3]+"','"+row[4]+"');"

        # Execute the SQL code
        cur.execute(sql, (
            pk, row[0], row[1], row[2], row[3],
            row[4]
        ))



# Commit the SQL code to the database
conn.commit()

# Close the cursor object
cur.close()

# Close the database connection
conn.close()

print("Database populated successfully!")