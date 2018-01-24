#! /bin/python

import re
import media
import fresh_tomatoes

# We have already collated the movie information and saved it in a CSV file
# called "movie_database.csv". We will read this in, parse each line (one movie)
# per line, and store the relevant information in a Movie class.

def parse_movie_information(movie_information):
    """
    Given a CSV delimited row:
      - split on commas,
      - remove non-essential characters (quotations and new lines)
      - returns a dictionary of movie information
    Note, we use the sun function from the package 're'.
    """

    # parse the movie information
    movie_clean = [re.sub("\"", "", x) for x in movie_information.split(",")]
    movie_information = {"title":movie_clean[0],
                         "release_year":movie_clean[1],
                         "poster_url":movie_clean[2],
                         "trailer_url":movie_clean[3]}

    # save an an instance of class Movie
    movie = media.Movie(movie_information['title'],
                        movie_information['poster_url'],
                        movie_information['trailer_url'])

    return movie
    
    
def read_database(filepath):
    """
       Reads a CSV file of move information.
       Returns a list of movie dictionaries with the clean movie information.
    """
    with open("movie_database.csv") as f:
        db = f.readlines()
    movies = [parse_movie_information(x.strip()) for x in db[1:]]

    return movies

       
fresh_tomatoes.open_movies_page(read_database("movie_database.csv"))
