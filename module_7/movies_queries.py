import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",

        "database": "movies",
    "raise_on_warnings": True
}

# Connect to the movies database
db = mysql.connector.connect(**config)

# Create a new cursor on the connection
cursor = db.cursor()

# Select all fields from the studio table
cursor.execute("SELECT * from studio")
# Use fetchall() method to fetch studio
studio = cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
# Use a for loop to print required studio columns
for studio in studio:
    print("Studio ID:", studio[0])
    print("Studio Name:", studio[1])
    print(" ")

# Select all fields from the genre table
cursor.execute("SELECT * from genre")
# Use fetchall() method to fetch genre
genre = cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
# Use a for loop to print required genre columns
for genre in genre:
    print("Genre ID:", genre[0])
    print("Genre Name:", genre[1])
    print(" ")

# Select the movie names for those movies that have a run time of less than two hours (120 minutes
cursor.execute("SELECT film_name, film_runtime from film where film_runtime < 120")
# Use fetchall() method to fetch film
film = cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
# Use a for loop to print required film columns
for film in film:
    print("Film Name:", film[0])
    print("Runtime:", film[1])
    print(" ")

# Select a list of film names, and directors ordered by director.
cursor.execute("SELECT film_name, film_director from film order by film_director")
# Use fetchall() method to fetch film
film = cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
# Use a for loop to print required film columns
for film in film:
    print("Film Name:", film[0])
    print("Director:", film[1])
    print(" ")

# Close the cursor
cursor.close()

# Close the connection
db.close()