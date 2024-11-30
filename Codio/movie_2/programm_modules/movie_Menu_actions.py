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


def print_random_movie(movies):
  """Displays a random movie from movies.

      Args:
          movies (list): the list with dictionaries of movie informations
      """
  random_index = random.randrange(len(movies))
  random_movie = movies[random_index]
  print("Here is a ranodm movie out of the Database:")
  print(f"{random_movie[KFN]}({random_movie[KFY]}): {random_movie[KFR]}")


def get_movie_stats(movies):
  average = get_average(movies)
  median = get_median(movies)
  best_movies = get_best_movies(movies)
  worst_movies = get_worst_movies(movies)
  print_movie_stats(average, best_movies, median, worst_movies)


def print_movie_stats(average, best_movies, median, worst_movies):
  print()
  print("The statistics are:")
  print(f"Average of rating: {average:.2f}")
  print(f"The median of rating is: {median}")
  print("the best movie/s is/are:")
  print_movies(best_movies)
  print("the worst movie/s is/are:")
  print_movies(worst_movies)


def get_average(movies):
  ratings = get_sorted_rating_list(movies)
  average = sum(ratings) / len(ratings)
  return average


def get_sorted_rating_list(movies):
  sorted_list = sort_movies_by_rating(movies)
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
  sorted_list = get_sorted_rating_list(movies)
  # finds the middle vlaue of the list (for the median)
  mid_index = len(sorted_list) // 2 - 1
  # when list is even
  if len(sorted_list) % 2 == 0:
    median = (sorted_list[mid_index] + sorted_list[mid_index + 1]) / 2
  # when lst is uneven
  else:
    median = sorted_list[mid_index]
  return median


def get_best_movies(movies):
  sorted_movie_list = sort_movies_by_rating(movies)
  sml = sorted_movie_list
  best_rating = sml[0][KFR]
  best_movies = []
  for i in range(len(sml)):
    if sml[i][KFR] == best_rating:
      best_movies.append(sml[i])
  return best_movies


def get_worst_movies(movies):
  sorted_movie_list = sort_movies_by_rating(movies)
  sml = sorted_movie_list
  worst_rating = sml[-1][KFR]
  worst_movies = []
  for i in range(len(sml)):
    if sml[i][KFR] == worst_rating:
      worst_movies.append(sml[i])
  return worst_movies


def print_movies_by_rating(movies):
  sorted_movies = sort_movies_by_rating(movies)
  for dict in sorted_movies:
    print_random_movie(dict)


def print_movies_by_year(movies):
  sorted_movies = sort_movies_by_year(movies)
  for dict in sorted_movies:
    print_random_movie(dict)


def filer_movies(movies):
  """soll filme nach
    - rating filtern (zeige alle filme rating über x an
    - year filtern (zeige alle filme ab 2001)
    - year filtern (zeige alle filme vor 2009)"""
  pass


if __name__ == "__main__":
  main()