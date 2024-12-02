import random
from programm_modules import movie_storage as ms
from programm_modules import movie_Menu_actions as mma


def execute_user_input(user_input, movies):
  """Takes the user_input and executes one of nine aktions

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
    # list all movies
  elif user_input == 2:
    # add movie
  elif user_input == 3:
    # delete_movie(movies)
  elif user_input == 4:
    # update_rating(movies)
  elif user_input == 5:
    # print_statistiks(movies)
  elif user_input == 6:
    # random_movie(movies)
  elif user_input == 7:
    # search_movie(movies)
  elif user_input == 8:
    # movies_sorted(movies)


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
  operations ={
    1 : mma.list_movies(movies),
    2 : ms.add_movie(),
    3 : ms.delete_movie(),
    4 : ms. update_movie(),
    5 : mma.get_movie_stats(movies),
    6 : mma.print_random_movie(movies),
    7 : mma.search_movie(movies),
    8 : mma.print_movies_sorted_by_rating(movies)
  }
  # print_menu gibt 1 - 8 aus, als string
  print("********** My Movies Database **********")



if __name__ == "__main__":
  main()