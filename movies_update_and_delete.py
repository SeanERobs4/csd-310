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

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))

# update method
def update():

    # Create cursor
    cursor = db.cursor()

    # Displaying existing records in database
    show_films(cursor, "DISPLAYING FILMS")

    # Perform Insertion of new movie
    cursor.execute("Insert into film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) values ('Star Wars', '1977', '121', 'George Lucas', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Perform Update of Alien movie
    cursor.execute("Update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where film_name = 'Alien';")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator movie from table
    cursor.execute("Delete from film where film_name = 'Gladiator';")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Calling update() function
update()