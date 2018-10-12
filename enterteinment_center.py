import media
import fresh_tomatoes

# Create new instances of movies
cinema_paradiso = media.Movie("Cinema Paradiso",
                              " famous Italian film director Salvatore Di Vita"
                              " returns home late one evening, where his"
                              " girlfriend sleepily tells him that his mother"
                              " called to say someone named Alfredo has died.",
                              "https://upload.wikimedia.org/wikipedia/en/8/86/CinemaParadiso.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=C2-GX0Tltgw")

once_upon_west = media.Movie("Once Upon a Time in the West",
                             " In the American Old West: a land battle"
                             " related to construction of a railroad,"
                             " and a mission of vengeance against a cold-blooded killer.",  # NOQA
                             "https://upload.wikimedia.org/wikipedia/en/a/a2/Once_upon_a_Time_in_the_West.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=MNGQ1hUyx-k")

the_sound_of_music = media.Movie("The Sound of Music",
                                 " Maria is a free-spirited"
                                 " young Austrian woman studying to"
                                 " become a nun at Nonnberg Abbey in Salzburg."
                                 " Her love of music and the mountains,"
                                 " her youthful enthusiasm and imagination,"
                                 " and her lack of discipline cause some"
                                 " concern among the nuns.",
                                 "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=lEcKXr3mJ_o")

the_godfather = media.Movie("The Godfather",
                            "In 1945, at his daughter Connie's wedding,"
                            " Don Vito Corleone hears requests in his"
                            " role as head of a New York crime family.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Godfather_ver1.jpg/210px-Godfather_ver1.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik&t=56s")  # NOQA

citzen_kane = media.Movie("Citizen Kane",
                          "In a mansion in Xanadu, a vast palatial"
                          " estate in Florida, the elderly Charles"
                          " Foster Kane is on his deathbed.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Citizenkane.jpg/220px-Citizenkane.jpg",  # NOQA
                          "https://youtu.be/1TmXN4aIGzc")  # NOQA

# Creates a html page displaying the movies created above
fresh_tomatoes.open_movies_page([cinema_paradiso, once_upon_west,
                                 the_sound_of_music, the_godfather,
                                 citzen_kane])
