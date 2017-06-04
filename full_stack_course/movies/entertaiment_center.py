
import fresh_tomatoes
import media

toy_story = media.Movie("Toy story",
			"A story of a child and his toys hat come to life",
			"https://www.google.es/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwj_rvizk6XUAhWDtRQKHZUJDywQjRwIBw&url=http%3A%2F%2Fgoogle.com%2Fsearch%3Ftbm%3Disch%26q%3DToy%2520Story&psig=AFQjCNFirR-uTdmiyDgCYN5pjx67H0RxTg&ust=1496698732565674",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)


avatar = media.Movie("Avatar", "A marine on an alien planet", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.trailer_youtube_url)
#toy_story.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
