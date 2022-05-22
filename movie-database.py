import sqlite3

# Class to store movie info
class Movie:
    
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


conn = sqlite3.connect('movie.db')

c = conn.cursor()

# Create movies table
c.execute("""CREATE TABLE movies (
    title text,
    genre text
)""")

#Insert functiom
def insert_mov(mov):
    with conn:
        c.execute("INSERT INTO movies VALUES (?, ?)", (mov.title, mov.genre))

# Retreive function
def get_movie_by_name(mov):
    c.execute("SELECT * FROM movies WHERE title=?", (mov,))
    return c.fetchall()

# Update functiom
def update_genre(mov, genre):
    with conn:
        c.execute("UPDATE movies SET genre = ? WHERE title = ?", (genre, mov.title))

#Remove function
def remove_mov(mov):
    with conn:
        c.execute("DELETE from movies WHERE title = ? AND genre = ?",
        (mov.title, mov.genre))

#Collumns in tables
mov_1 = Movie('Titantic', 'Drama')
mov_2 = Movie('Rocky', 'Action')
mov_3 = Movie('Frozen', 'Adventure')

insert_mov(mov_1)
insert_mov(mov_2)
insert_mov(mov_3)

update_genre(mov_1, 'Romance')

remove_mov(mov_2)

get_mov = get_movie_by_name('Frozen')
print(get_mov)


conn.close()

#Class to store director info
class Director():

    def __init__(self, first, last, movie):
        self.first = first
        self.last = last
        self.movie = movie

conn = sqlite3.connect('director.db')

c = conn.cursor()

c.execute("""CREATE TABLE directors (
    first text,
    last text,
    movie text
)""")

#Insert function
def insert_dir(dir):
    with conn:
        c.execute("INSERT INTO directors VALUES (?, ?, ?)", (dir.first, dir.last, dir.movie))


#Retrieve function
def get_director_by_name(movie):
    c.execute("SELECT * FROM directors WHERE movie=?", (movie,))
    return c.fetchall()

#Update function
def update_movie(dir, movie):
    with conn:
        c.execute("UPDATE directors SET movie = ? WHERE first = ? AND last = ?", (movie, dir.first, dir.last))

#Remove function
def remove_dir(dir):
    with conn:
        c.execute("DELETE from directors WHERE first = ? AND last=?",
        (dir.first, dir.last))


#Collumns in table
dir_1 = Director('James', 'Cameron', 'Titantic')
dir_2 = Director('John', 'Avildsen', 'Rocky')
dir_3 = Director('Chris', 'Buck', 'Frozen')

insert_dir(dir_1)
insert_dir(dir_2)
insert_dir(dir_3)

update_movie(dir_3, 'Tarzan')

remove_dir(dir_2)

get_dir = get_director_by_name('Titantic')
print(get_dir)

conn.close()
