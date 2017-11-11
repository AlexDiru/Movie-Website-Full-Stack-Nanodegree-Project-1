import media
import fresh_tomatoes

# Create the movies
crows_zero = media.Movie("Crows Zero", "Fighting in Suzuran",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Crowszero.jpg/220px-Crowszero.jpg",
                         "https://www.youtube.com/watch?v=6H3CMjsX2CE")
crows_zero_2 = media.Movie("Crows Zero II", "Suzuran vs Housen",
                           "http://blueprintreview.co.uk/wp-content/uploads/2012/07/Crows-Zero-2-movie-poster.jpg",
                           "https://www.youtube.com/watch?v=hTPZW28r_K0")
crows_explode = media.Movie("Crows Explode", "Genji's graduated",
                            "http://www.martialartsmoviejunkie.com/wp-content/uploads/2014/01/Crows-Explode-Poster.jpg",
                            "https://www.youtube.com/watch?v=fRMxLsNn-ZY")

# Add to list
movies = [crows_zero, crows_zero_2, crows_explode]

# Create HTML
fresh_tomatoes.open_movies_page(movies)
