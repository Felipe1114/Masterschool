import json as js
DATAPATH = "../programm_files/movie_storage.json"


def get_movies() -> dict:
  """
  Returns a dictionary of dictionaries that
  contains the movies information in the database.

  The function loads the information from the JSON
  file and returns the data.

  For example, the function may return:
  {
    "Titanic": {
      "rating": 9,
      "year": 1999
    },
    "..." {
      ...
    },
  }
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


def add_movie(title:str, year:int, rating:float) -> dict:
  """
  Adds a movie to the movies database.
  Loads the information from the JSON file, add the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()
  movie_infos = {}
  movie_infos["year"] = year
  movie_infos["rating"] = rating
  movies[title] = movie_infos
  save_movies(movies)

def delete_movie(title):
  """
  Deletes a movie from the movies database.
  Loads the information from the JSON file, deletes the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()
  movies.pop(title)
  save_movies(movies)


def update_movie(title, rating):
  """
  Updates a movie from the movies database.
  Loads the information from the JSON file, updates the movie,
  and saves it. The function doesn't need to validate the input.
  """
  movies = get_movies()
  movies[title]["rating"] = rating
  save_movies(movies)



print(get_movies())