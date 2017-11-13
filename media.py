import webbrowser


class Movie():
    """Class to represent a movie

    Stores the title, storyline, URL to the poster and a URL to the
    trailer (on YouTube)

    Attributes:
        title (str): Title of the movie
        storyline (str): Storyline of the movie
        poster_image_url (str): Image URL of the movie poster
        trailer_youtube_url (str): Trailer URL of the movie on YouTube

    Future work:
        May be refactored to Video if TV Shows are implemented
        Movie derives from Video
        TV Show derives from Video

    """

    def __init__(self, title, storyline, poster_image_url, trailer_url):
        """Initialises the class with four string parameters; exceptions are
        thrown if any are empty

        Args:
            title (str): Title of the movie
            storyline (str): Storyline of the movie
            poster_image_url (str): Image URL of the movie poster
            trailer_url (str): Trailer URL of the movie

        """

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
