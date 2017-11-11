import webbrowser


# Class to represent a movie
# Future work:
# May be refactored to Video if TV Shows are implemented
# Movie derives from Video
# TV Show derives from Video
class Movie():
    # Four string parameters, exceptions are thrown if any are empty
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        # Error checking
        if title == "":
            raise ValueError("Movie title is empty")
        if storyline == "":
            raise ValueError("Storyline is empty")
        if poster_image_url == "":
            raise ValueError("Poster Image URL is empty")
        if trailer_url == "":
            raise ValueError("Trailer URL is empty")

        # Set params
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url
