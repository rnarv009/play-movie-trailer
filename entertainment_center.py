import fresh_tomatoes
import media
#toy_story=media.Movie("Toy Story",
#                      "A story of a boy and his toys that come to life",
#                      "http://upload.wikimedia.org/wikipedia/en/13/Toy_story.jpg",
#                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#avatar=media.Movie("Avatar",
#                   "A marin on an alien planet",
#                   "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser",
#                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.show_trailer()
my_name_is_khan=media.Movie("MY NAME IS KHAN",
                            "situation of the muslim people in US after 26/11 ",
                            "https://upload.wikimedia.org/wikipedia/en/5/5d/My_Name_Is_Khan_film_poster.jpg",
                            "https://www.youtube.com/watch?v=nqxgYT3TYzY")
ddlj=media.Movie("DDLJ",
                 "SRK best love story movie ",
                 "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                 "https://www.youtube.com/watch?v=c25GKl5VNeY")
veer_zaara=media.Movie("VEER ZAARA",
                 "SRK and PREITY ZINTA best love story movie ",
                 "https://upload.wikimedia.org/wikipedia/en/c/cb/Veerzaara.jpg",
                 "https://www.youtube.com/watch?v=x76AewWDKPw")
three_Idiots=media.Movie("3 Idiots",
                 "AMIR KHAN best movie ever ",
                 "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                 "https://www.youtube.com/watch?v=K0eDlFX9GMc")
#my_name_is_khan.show_trailer()
movies=[my_name_is_khan,ddlj,veer_zaara,three_Idiots]
fresh_tomatoes.open_movies_page(movies)

                            

