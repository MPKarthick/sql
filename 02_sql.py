# create sqlite3 database and table
import  sqlite3

# create new database if not exist
conn = sqlite3.connect("new.db")

# create sql cursor obj to execute sql queries
cursor = conn.cursor()

try:
    # inserting values into the table
    cursor.execute("INSERT INTO	population VALUES('New York City','NY',8400000)")
    cursor.execute("INSERT INTO population	VALUES('San	Francisco','CA',800000)")

    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oops...! something went wrong try again...!")
# close the connection
conn.close()

# or below insert code can also be used for inserting value
# commit and close will be done automatically when we use with statement

# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     # inserting values into the table
#     c.execute("INSERT INTO	population VALUES('New York City','NY',8400000)")
#     c.execute("INSERT INTO population	VALUES('San	Francisco','CA',800000)")