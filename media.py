import webbrowser

# Class for Movies including Title, Storyline, Poster Image URL and Trailer
class Movie():
       def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Show the trailers by clicking on the posterimage
def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
