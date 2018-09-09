#Defines the Movie class that contains the details of a movie.
import webbrowser

# Class for Movies including Title, Storyline, Poster Image URL and Trailer
class Movie():
       def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
# Initialises Movie class instance variables.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Shows the trailers by clicking on the posterimage
def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
