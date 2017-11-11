import webbrowser

class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        #Error checking
        if title == "":
            raise ValueError("Movie title is empty")
        if storyline == "":
            raise ValueError("Storyline is empty")
        if poster_image_url == "":
            raise ValueError("Poster Image URL is empty")
        if trailer_url == "":
            raise ValueError("Trailer URL is empty")
        
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url