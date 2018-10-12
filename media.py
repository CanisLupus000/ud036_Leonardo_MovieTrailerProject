class Movie:
    """Constructs a new instance of movie.
        Args:
            movie_title (string) : The new movie's title
            movie_storyline (string) : Short paragraph
                                        describing the new movies story
            movie_poster_url (string) : url to a image of the
                                        new movie's poster
            movie_trailer_youtube (string) : url to a youtube video
                                                of the new movie's trailer
    """

    def __init__(self, movie_title, movie_storyline, movie_poster_url,
                 movie_trailer_youtube):

        self.trailer_youtube_url = movie_trailer_youtube
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.storyline = movie_storyline
