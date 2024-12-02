import json as js
import movie_Menu_actions as mma

DATAPATH = "../programm_files/movie_storage.json"

# der punkt vor /programm mus noch weg, damit es ind er main funktion funktioniert
KEY_FOR_YEAR = "year"
KFY = KEY_FOR_YEAR
KEY_FOR_RATING = "rating"
KFR = KEY_FOR_RATING
KEY_FOR_NAME = "name"
KFN = KEY_FOR_NAME


def get_movies() -> list:
  """
  Returns a dictionary of dictionaries that
  contains the movies information in the database.

  The function loads the information from the JSON
  file and returns the data.
  """
  with open(DATAPATH, "r") as json_data:
    movies = js.load(json_data)
  return movies


def save_movies(movies):
  """
  Gets all your movies as an argument and saves them to the JSON file.
  """
  with open(DATAPATH, "w") as json_data:
    js.dump(movies, json_data, indent=4)


def add_movie():
  """
  Adds a movie to the movies database.
  Loads the information from the JSON file, add the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()
  new_movie = {}

  #kann man in "movie_Menu_actions" verlagern
  while True:
    try:
      new_movie[KFN] = input("Type in a movie name: ")
      new_movie[KFY] = int(input("Wich was the release year?(int): "))
      new_movie[KFR] = float(input("Type in your rating.(float): "))
      break
    except ValueError as e:
      print(f"Input must be a number: {e}")

  movies.append(new_movie)

  save_movies(movies)


def delete_movie():
  """
  Deletes a movie from the movies database.
  Loads the information from the JSON file, deletes the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()

  movie_title = mma.get_movie_name(movies)

  searched_dict, index = find_dict_by_name(movies, movie_title)
  del movies[index]
  save_movies(movies)



def update_movie():
  """
  Updates a movie from the movies database.
  Loads the information from the JSON file, updates the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()

  movie_name = mma.get_movie_name(movies)
  movie_rating = mma.get_movie_rating()

  searched_dict, index = find_dict_by_name(movies, movie_name)
  movies[index][KFR] = movie_rating
  save_movies(movies)


def find_dict_by_name(movies:list, searched_name:str) -> tuple:
  """Iterates thrue all dicts in the list(movies).
  Checks, if searched name is a value from the key "name".
  searching is case insensitive
  If so, it returns the whole dict, with the key-value "movie_name"

  Args:
    movies(list): a list, of dictionaries, with movie informations
    searched_name: the value of the key "name" of a movie-dictionary

  Returns:
    dict: a single dictionary, with informations about one film
    i: the index of the searched dict in the movie-list
  """
  for i in range(len(movies)):
    if movies[i][KFN].lower == searched_name.lower:
      return movies[i], i
  raise ValueError("Given name not in movie-list. Please give an existing name")






