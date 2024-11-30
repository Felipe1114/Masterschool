import random
import movie_storage as ms
KEY_FOR_YEAR = "year"
KFY = KEY_FOR_YEAR
KEY_FOR_RATING = "rating"
KFR = KEY_FOR_RATING
KEY_FOR_NAME = "name"
KFN = KEY_FOR_NAME


def main():
  movies = ms.get_movies()
  print(sort_movies_by_year(movies))


def search_movie(movies:list):
  """The user gives an input(movie name), than the funktion prints the movie,
  with its release year and ranking

      Args:
          movies (list): a list of movie dictionarys

      Returns:
          None
      """
  while True:
    try:
      searched_name = input("Wich movie are you searching for?: ")
      searched_movie, index = ms.find_dict_by_name(movies, searched_name)
      print_single_movie(searched_movie)
    except ValueError as e:
      print("Error:", e)


def print_single_movie(movie:dict):
  """Prints a movie, with its release year and ranking

      Args:
      movie(dict): a dictionary with all informations about one movie
      """
  print(f"{movie[KFN]}({movie[KFY]}): {movie[KFR]}")


def print_movies(list):
  """prints a list of movies

    Args:
      list(list): a given list of dictionaries with movie informations
  """
  for movie in list:
    print(f"{movie[KFN]}({movie[KFY]}): {movie[KFR]}")

# die sort fruntioen kann man noch zusammenfügen, in dem man
# den key als parameter als argument einfügt
def sort_movies_by_rating(movies):
  sorted_movies = sorted(movies, key=lambda dict:dict[KFR], reverse=True)
  return sorted_movies


def sort_movies_by_year(movies):
  sorted_movies = sorted(movies, key=lambda dict:dict[KFY], reverse=True)
  return sorted_movies


def sort_movies_by_name(movies):
  sorted_movies = sorted(movies, key=lambda dict: dict[KFN], reverse=True)
  return sorted_movies

def movies_sorted(movies):
  """Sorts the movies by rating from highest to lowest and prints the sorted list.

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          None
      """
  highest_key = ""
  copy_movies = movies.copy()
  while len(list_sorted_movies) < len(movies):
    highest_val = 0
    for key, val in copy_movies.items():
      if val > highest_val:
        highest_val = val
        highest_key = key
    del copy_movies[highest_key]
    list_sorted_movies[highest_key] = highest_val


if __name__ == "__main__":
  main()