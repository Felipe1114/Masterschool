import random
from programm_modules import movie_storage as ms

#========================DELETE unten===================================
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


def print_single_ranked_movie(key, movies: type(dict)):
  """Prints a movie, with its ranking

      Args:
          key (str): The name of the movie.
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          None
      """
  print(key, movies[key], sep = " : ")


def movies_sorted(movies):
  """Sorts the movies by rating from highest to lowest and prints the sorted list.

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          None
      """
  dic_sorted_movies = {}
  highest_key = ""
  copy_movies = movies.copy()
  while len(dic_sorted_movies) < len(movies):
    highest_val = 0
    for key, val in copy_movies.items():
      if val > highest_val:
        highest_val = val
        highest_key = key
    del copy_movies[highest_key]
    dic_sorted_movies[highest_key] = highest_val
  print_ranked_movies(dic_sorted_movies)
  execute_user_input(int(print_menu(back_to_menu())), movies)


def random_movie(movies):
  """Displays a random movie from movies.

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          None
      """
  movie_list = make_movie_list(movies)
  index_list = random.randrange(len(movie_list))
  random_movie = movie_list[index_list]
  print("Here is a ranodm movie out of the Database:")
  print(f"Movie: {random_movie}")
  execute_user_input(int(print_menu(back_to_menu())), movies)


def make_movie_list(movies):
  """Makes a list of the movie names(keys) from dictionary (movies)

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          a list of all movie names(keys)
     """
  movie_list = []
  for key in movies:
    movie_list.append(key)
  return movie_list


#========================DELETE oben ===================================













def make_rating_list(movies):
  """Makes a list of the movie ratings(values) from dictionary (movies)

          Args:
              movies (dict): the dictionary with the movies and their rankings

          Returns:
              a list of all movie ratings(values)
         """
  value_list = []
  for key in movies:
    value_list.append(movies[key])
  return value_list


def sort_list(list):
  """sorts a given list from the hightest to the lowest

      Args:
          list(list): a list with the movie ratings

      Returns:
            a list of all movie ratings, sortet form hightest to lowest
  """
  list.sort(reverse=True)
  return list


def sum_list(list):
  """sums all numbers of a list

      Args:
          list(list): al list with all movie ratings

      Returns:
          the sum of all ratings
  """
  sum = 0
  for num in list:
    sum += num
  return sum


def avergae(movies):
  """calculates the average from all ratings(values) of movies(dict)

       Args:
           movies (dict): the dictionary with the movies and their rankings

       Returns:
           the average of the movie ratings(values)
  """
  value_list = make_rating_list(movies)
  average = sum_list(value_list) / len(value_list)
  return average


def make_median(movies):
  """calculates the median from all ratings(values) of movies(dict)

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          the median of the movie ratings(values)
 """
  sorted_list = sort_list(make_rating_list(movies))
  # finds the middle vlaue of the list (for the median)
  mid_index = len(sorted_list) // 2 - 1
  # when list is even
  if len(sorted_list) % 2 == 0:
    median = (sorted_list[mid_index] + sorted_list[mid_index+1]) / 2
  # when lst is uneven
  else:
    median = sorted_list[mid_index]
  return median


def find_best_movies(movies):
  """gives the movie/s, with the best rating/s

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          a dictionary with the best movies: names(keys); ratings(values)
  """
  best_key = max(movies, key = movies.get)
  movies_copy = movies.copy()
  del movies_copy[best_key]
  best_key_copy = max(movies_copy, key = movies_copy.get)
  best_movies = {best_key : movies[best_key]}
  while True:
    if movies_copy[best_key_copy] == movies[best_key]:
      best_movies[best_key_copy] = movies_copy[best_key_copy]
      del movies_copy[best_key_copy]
    else:
      break
  return best_movies


def find_worst_movies(movies):
  """gives the movie/s, with the worst rating/s

          Args:
              movies (dict): the dictionary with the movies and their rankings

          Returns:
              a dictionary with the worst movies: names(keys); ratings(values)
      """
  worst_key = min(movies, key = movies.get)
  movies_copy = movies.copy()
  del movies_copy[worst_key]
  worst_key_copy = min(movies_copy, key=movies_copy.get)
  worst_movies = {worst_key : movies[worst_key]}
  while True:
    if movies_copy[worst_key_copy] == movies[worst_key]:
      worst_movies[worst_key_copy] = movies_copy[worst_key_copy]
      del movies_copy[worst_key_copy]
    else:
      break
  return worst_movies


def print_statistiks(movies):
  """calculates and prints the average, median from all movies, the best and worst movie/s

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  average = avergae(movies)
  median = make_median(movies)
  best_movies = find_best_movies(movies)
  worst_movies = find_worst_movies(movies)
  print()
  print("The statistics are:")
  print(f"Average of rating: {average:.2f}")
  print(f"The median of rating is: {median}")
  print("the best movie/s is/are:")
  print_movies_and_ratings(best_movies)
  print("the worst movie/s is/are:")
  print_movies_and_ratings(worst_movies)
  execute_user_input(int(print_menu(back_to_menu())), movies)


def update_rating(movies):
  """updates the rating from a given movie(input)

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
            none
  """
  print_movies_and_ratings(movies)
  selected_movie = input("Wich of these movie ratings, you want to update? ")
  new_rating = float(input("What is the new rating?(float) "))
  movies[selected_movie] = new_rating
  execute_user_input(int(print_menu(back_to_menu())), movies)


def delete_movie(movies):
  """Deletes a movie name(key) from the dictionary movies

          Args:
              movies (dict): the dictionary with the movies and their rankings

          Returns:
                none
  """
  print_movie_list(movies)
  del_movie = input("Wich movie, from this list, you want delete?:")
  del movies[del_movie]
  execute_user_input(int(print_menu(back_to_menu())), movies)


def add_movie(movies):
  """Adds a new movie name(key) and its rating(value) to movies(dictionary)

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  new_movie = input("Whats the name of the movie?: ")
  rating = float(input("What is its rating?(float): "))
  movies[new_movie] = rating
  execute_user_input(int(print_menu(back_to_menu())), movies)


def list_all_movies(movies : dict):
  """prints all movies(keys) and their ratings(values) from movies(dictionary)

      Args:
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  print_movies_and_ratings(movies)
  execute_user_input(int(print_menu(back_to_menu())), movies)


def print_movies_and_ratings(movies):
  """prints all movie names(keys) and their ratings(values) from movies(dictionary)

      Args:
           movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  for key in movies.keys():
    print(key, movies[key], sep = " : ")


def print_movie_list(movies):
  """prints all movie names(keys) from movies(dictionary)

      Args:
           movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  print()
  for key in movies.keys():
    print(key)


def execute_user_input(user_input, movies):
  """Takes the user_input and executes on of eight aktions

      Args:
          user_input (int): the command for a specific aktion of the programm
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  if user_input == 0:
    print("bye")
    exit()
  if user_input == 1:
    list_all_movies(movies)
  if user_input == 2:
    add_movie(movies)
  if user_input == 3:
    delete_movie(movies)
  if user_input == 4:
    update_rating(movies)
  if user_input == 5:
    print_statistiks(movies)
  if user_input == 6:
    random_movie(movies)
  if user_input == 7:
    search_movie(movies)
  if user_input == 8:
    movies_sorted(movies)


def back_to_menu():
  """Gives a command to the User, to press enter to go back to menu

      Args:
          none

      Returns:
          an empty String(""; its equal, what the user prints, but in best case, it is only an empty string)
      """
  return input("\npress Enter to go back to menu")


def print_menu(user_input = ""):
  """Displays the Menu to the user with the input commands

      Args:
          user_input (str): the empty string ftrom "Back_to_menu"

      Returns:
          the user inpt with the command for a programm aktion(str)
  """
  print("")
  print("Menu:")
  print("0. Exit")
  print("1. List movies")
  print("2. Add movie")
  print("3. Delete movie")
  print("4. Update movie")
  print("5. Stats")
  print("6. Random movie")
  print("7. Search movie")
  print("8. Movies sorted by rating")
  return input("Enter choice (1-8): ")


def main():
  """Executes the user_input(str); contains movies(dictionary)

  Args:
  none

  Returns:
  none
  """
movies = ms.get_movies()
# print_menu gibt 1 - 8 aus, als string
print("********** My Movies Database **********")
execute_user_input(int(print_menu()), movies)


if __name__ == "__main__":
  main()