from termios import VLNEXT

from programm_modules import movie_storage as ms
from programm_modules import movie_Menu_actions as mma




def main():
  """Executes the user_input(str); contains movies(dictionary)

  Args:
  none

  Returns:
  none
  """
  print("********** Welcome to my Movies Database **********")

  movies = ms.get_movies()

  while True:
    operations ={
      0 : exit(),
      1 : mma.list_movies(movies),
      2 : ms.add_movie(),
      3 : ms.delete_movie(),
      4 : ms. update_movie(),
      5 : mma.get_movie_stats(movies),
      6 : mma.print_random_movie(movies),
      7 : mma.search_movie(movies),
      8 : mma.print_movies_sorted_by_rating(movies)
    }

    print_menu()


def print_menu():
  """Displays the Menu to the user with the input commands

      Args:
          user_input (str): the empty string ftrom "Back_to_menu"

      Returns:
          the user inpt with the command for a programm aktion(str)
  """
  print("\n===Menu:===\n"
        "\t0. Exit\n"
        "\t1. List movies\n"
        "\t2. Add moives\n"
        "\t3. Delete movie\n"
        "\t4. Update movie\n"
        "\t5. stats\n"
        "\t6. Random movie\n"
        "\t7. Search movie\n"
        "\t8. Movies sorted by rating")

  return get_user_input()


def get_user_input():
  """gets a number between 0 and 8 from user
  If input is invalid, or out of range, an error is risen

  :return: user_input(a number between 1 - 8. Will be used, to choose a programm action)
  """
  while True:
    try:
      return validade_user_input()
    except ValueError as e:
      print(e)


def validade_user_input():
  """gets an input from user and changes its type to integer.
  If input out of range, or not valid(string), an ValueError is risen

  :return: user_input(0-8)
  """
  user_input = int(input("What do you want to do?(0-8): "))

  if 8 < user_input < 0:
    raise ValueError("Error! Input must be between 0 and 8.")

  return user_input




# hier neuen code aufsetzten
def execute_user_input(user_input):
  """Takes the user_input and executes one of nine aktions

      Args:
          user_input (int): the command for a specific aktion of the programm
          movies (dict): the dictionary with the movies and their rankings

      Returns:
          none
  """
  if user_input == 0:
    # exit
  elif user_input == 1:
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






if __name__ == "__main__":
  main()