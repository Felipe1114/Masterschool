import random
from programm_modules import movie_storage as ms

#========================DELETE unten===================================


#========================DELETE oben ===================================


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