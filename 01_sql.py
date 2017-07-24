# create sqlite3 database and table

import sqlite3

# create new database if not exist
conn = sqlite3.connect("new.db")

# create sql cursor obj to execute sql queries
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)
# close the database connection
conn.close()