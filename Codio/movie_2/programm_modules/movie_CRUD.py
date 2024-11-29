import random
import movie_storage as ms


def main():
  movies = ms.get_movies()
  print(movies)


def search_movie(movies:dict):
  """The user gives an input(movie name), than the funktion prints the movie, with its ranking

      Args:
          movies (dict): the dictionary wihth the movies and their rankings

      Returns:
          None
      """
  searched_movie = input("Wich movie are you searching for?: ")
  for key in movies.keys():
    if searched_movie.lower() == key.lower():
      print_single_ranked_movie(key, movies)
  execute_user_input(int(print_menu(back_to_menu())), movies)



if __name__ == "__main__":
  main()