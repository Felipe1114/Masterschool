import random
from.import movie_storage as ms
import copy

KEY_FOR_YEAR = "year"
KFY = KEY_FOR_YEAR
KEY_FOR_RATING = "rating"
KFR = KEY_FOR_RATING
KEY_FOR_NAME = "name"
KFN = KEY_FOR_NAME


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
  return f"{movie[KFN]}({movie[KFY]}): {movie[KFR]}"


def list_up_movies(list):
  """prints a list of movies

    Args:
      list(list): a given list of dictionaries with movie informations
  """

  text = ""
  for movie in list:
    text = text + f"{movie[KFN]}({movie[KFY]}): {movie[KFR]}" + "\n" # print engine einbauen

  return text



def sort_movies(movies, key):
  """Sorts the List(movies) by rating, year or name

  :param movies: a list of dictionaries with movie informations
  :param key: the key for rating, year or name
  :return: the sorted list of dictionaries
  """
  sorted_movies = sorted(movies, key=lambda dict:dict[key], reverse=True)
  return sorted_movies


def print_random_movie(movies):
  """Displays a random movie from movies.

      Args:
          movies (list): the list with dictionaries of movie informations
      """
  random_index = random.randrange(len(movies))
  random_movie = movies[random_index]

  return (f"Here is a ranodm movie out of the Database:\n"
          f"{random_movie[KFN]}({random_movie[KFY]}): {random_movie[KFR]}")


def get_movie_stats(movies):
  """Calculates and diyplays average rating, median rating, best and worst movie rating

  :param movies: a list of dictionaries with movie informations
  """
  average = get_average(movies)
  median = get_median(movies)
  best_movies = get_best_movies(movies)
  worst_movies = get_worst_movies(movies)

  print_movie_stats(average, best_movies, median, worst_movies)


def print_movie_stats(average, best_movies, median, worst_movies):
  """Displays all movie stats

  :param average: average movie ratings
  :param best_movies: movie(s) with the best rating
  :param median: median movie ratings
  :param worst_movies: movie(s) with the worst rating
  :return: a long string with all statistics
  """
  best_movie = list_up_movies(best_movies)
  worst_movie = list_up_movies(worst_movies)
  return (f"\nThe statistics are:" # warum wird hier nichts zurück gegeben?
          f"Average of rating: {average:.2f}\n"
          f"The median of rating is: {median}\n"
          f"--------\nthe best movie/s is/are:\n"
          f"{best_movie}"
          f"he worst movie/s is/are:"
          f"{worst_movie}")



def get_average(movies):
  """calcultes the average of all movie ratings

  :param movies: a list of dictionaries with movie informations
  :return: the average of all movie ratings
  """
  ratings = sort_list_by_rating(movies)
  average = sum(ratings) / len(ratings)

  return average


def sort_list_by_rating(movies):
  """sorts the list(movies) by its ratings in the dicionaries

  :param movies: a list of dictionaries with movie informations
  :return: a list of dictionaries, sorted by its values of the keys[ratings]
  """
  sorted_list = sort_movies(movies, KFR)
  rating_list = []

  for dict in sorted_list:
    rating_list.append(dict[KFR])

  return rating_list


def get_median(movies):
  """calculates the median from all ratings(values) of movies(dict)

        Args:
            movies (dict): the dictionary with the movies and their rankings

        Returns:
            the median of the movie ratings(values)
   """
  sorted_list = sort_list_by_rating(movies)

  # finds the middle vlaue of the list (for the median)
  mid_index = len(sorted_list) // 2 - 1

  # when list is even
  if len(sorted_list) % 2 == 0:
    median = (sorted_list[mid_index] + sorted_list[mid_index + 1]) / 2

  # when list is uneven
  else:
    median = sorted_list[mid_index]
  return median


def get_best_movies(movies):
  """gets the best movie(s) - by rating - in the list (movies)

  :param movies: a list of dictionaries with movie informations
  :return: movie(s) with the highest rating
  """
  sorted_movie_list = sort_movies(movies, KFR)
  sml = sorted_movie_list
  best_rating = sml[0][KFR]
  best_movies = []
  for i in range(len(sml)):
    if sml[i][KFR] == best_rating:
      best_movies.append(sml[i])
  return best_movies


def get_worst_movies(movies):
  """gets the worst movie(s) - by rating - in the list (movies)

  :param movies: a list of dictionaries with movie informations
  :return: movie(s) with the highest rating
  """
  sorted_movie_list = sort_movies(movies, KFR)
  sml = sorted_movie_list
  worst_rating = sml[-1][KFR]
  worst_movies = []

  for i in range(len(sml)):
    if sml[i][KFR] == worst_rating:
      worst_movies.append(sml[i])

  return worst_movies


def print_movies_sorted_by_rating(movies):
  """prints movies, sorted by rating (high to low)

  :param movies: a list of dictionaries with movie informations
  """
  sorted_movies = sort_movies(movies, KFR)

  return list_up_movies(sorted_movies)



def filter_movies(movies):
  """filters a deep copy of list(movies) by the filter values given by user

  :param movies: a list of dictionaries with movie informations
  :return: a filtred list of movies
  """
  minimum_rating, start_year, end_year = get_filter_input()
  movies_copy = copy.deepcopy(movies)

  if len(minimum_rating) > 0: filter_rating(movies_copy, minimum_rating)

  if len(start_year) == 0: filter_by_end_year(movies_copy, end_year)
  elif len(end_year) == 0: filter_by_start_year(movies_copy, start_year)
  else: filter_by_start_and_end_year(movies_copy, start_year, end_year)

  return movies_copy


def get_filter_input():
  """
  gets the filter values from user. Changes types form input to float or integer
  :return: input in correct type
  """
  while True:
    try:
      minimum_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
      start_year = input("Enter start year (leave blank for no start year): ")
      end_year = input("Enter end year (leave blank for no end year): ")

      if len(minimum_rating) > 0:
        minimum_rating = float(minimum_rating)
      if len(start_year) > 0:
        start_year = int(start_year)
      if len(end_year) > 0:
        end_year = int(end_year)

      return minimum_rating, start_year, end_year

    except ValueError as e:
      print(f"Input must be empty or an number: {e}")


def filter_rating(movies_copy, minimum_rating):
  """makes a copy of movies and deletes all elements in the list,
  wich ratings are under minimum_rating

  Args:
    movies_copy(list): a list of dictionaries with movie informations
    minimum_rating(float): rating number, for filtering movies with lesser rating
    """
  for i in range(len(movies_copy)):
    if movies_copy[i][KFR] < minimum_rating:
      del movies_copy[i]

  return movies_copy


def filter_by_end_year(movies_copy, end_year):
  """Filters all movies, with release years higher than end_year, out of movies_copy

  Args:
    movies_copy(list): copy of the list "movies".
    end_year(int): an integer, representing an release year

  Returns:
    movies_copy(list): a modified version of the list "moves_copy"
  """
  for i in range(len(movies_copy)):

    if movies_copy[i][KFY] < end_year:
      continue
    else:
      del movies_copy[i]

  return movies_copy


def filter_by_start_year(movies_copy, start_year):
  """Filters all movies, with release years lower than start_year, out of movies_copy

    Args:
      movies_copy(list): copy of the list "movies".
      start_year(int): an integer, representing an release year

    Returns:
      movies_copy(list): a modified version of the list "moves_copy"
    """
  for i in range(len(movies_copy)):

    if start_year < movies_copy[i][KFY]:
      continue
    else:
      del movies_copy[i]

  return movies_copy


def filter_by_start_and_end_year(movies_copy, start_year, end_year):
  """Filters all movies, with release years out ouf give range, out of movies_copy

    Args:
      movies_copy(list): copy of the list "movies".
      end_year(int): an integer, representing an release year
      start_year(int): an integer, representing an release year

    Returns:
      movies_copy(list): a modified version of the list "moves_copy"
    """
  for i in range(len(movies_copy)):

    if start_year < movies_copy[i][KFY] < end_year:
      continue
    else:
      del movies_copy[i]

  return movies_copy


def get_movie_informations(new_movie):
  while True:
    try:
      new_movie[KFN] = input("Type in a movie name: ")
      new_movie[KFY] = int(input("Wich was the release year?(int): "))
      new_movie[KFR] = float(input("Type in your rating.(float): "))
      break
    except ValueError as e:
      print(f"Input must be a number: {e}")


def get_user_input_for_name():
  """takes from user a movie name

  :return:
  """
  movie_name = input("Type in a movie name: ")
  return movie_name


def is_name_in_movies(movie_name, movies):
  """Validades given movie name, if it is in list(movies)

  :param movie_name: movie name, to check if it is in movies
  :param movies: a list of dictionaries, with movie informations
  :return: None
  """
  name_is_valid = False
  for movie in movies:
    if movie_name == movie[KFN]:
      name_is_valid = True

  if name_is_valid:
    return
  else:
    raise ValueError("Error: Movie name is not in movie list!")


def get_movie_name(movies):
  """gets movie name by user input and valides it

  :param movies: a list of dictionaries with movie informations
  :return: the validated movie title
  """
  while True:
    try:
      movie_title = get_user_input_for_name()
      is_name_in_movies(movie_title, movies)
      break
    except ValueError as e:
      print(e)
  return movie_title


def get_movie_rating():
  while True:
    try:
      movie_rating = float(input("Type in your rating(float): "))
      return movie_rating
    except ValueError as e:
      print(f"Input must be a float: {e}")
