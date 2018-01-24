#! /bin/python

# Class Movie
# Needs to have class-level variables:
#   - title, trailer_youtube_url, poster_image_url

class Movie():
    """
    Creates an object of class Movie, which stores movie metadata:
      - the moie title
      - a link to the movie poster
      - a link to the movie trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
