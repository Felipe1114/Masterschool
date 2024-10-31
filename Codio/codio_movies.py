import random
from re import search

from macholib.mach_o import lc_str

'''  Aufgaben:
  x Menu
  x nach auswahl wieder zurück zu menu
  x Alle Filme auflisten
  x einen Film hinzufügen
  x einen film löschen
  x einen film updaten (die wertung ändern)
  x die statistiken anzeigen:
  x - durchschnitt, median, bester, schlechtester
  x einen zufälligen film printen
  nach einem film suchen (case insensitiv)
  x filme nach rating anzeigen
  '''
def search_movie(movies: type(dict)):
    searched_movie = input("Wich movie are you searching for?: ")
    for key in movies.keys():
        if searched_movie.lower() == key.lower():
            print_single_ranked_movie(key, movies)
    what_to_do(int(print_menu(back_to_menu())), movies)



def print_single_ranked_movie(key, movies: type(dict)):
    print(key, movies[key], sep = " : ")


def print_ranked_movies(dic_sorted_movies):
    print("\n")
    print("Here are al Movies, ranked from best to worst:")
    for key in dic_sorted_movies:
        print(key, dic_sorted_movies[key], sep = " : ")

def movies_sorted(movies):
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
    what_to_do(int(print_menu(back_to_menu())), movies)

def random_movie(movies):
    movie_list = make_movie_list(movies)
    index_list = random.randrange(len(movie_list))
    random_movie = movie_list[index_list]
    print("Here is a ranodm movie out of the Database:")
    print(f"Movie: {random_movie}")
    what_to_do(int(print_menu(back_to_menu())), movies)

def make_movie_list(movies):
    movie_list = []
    for key in movies:
        movie_list.append(key)
    return movie_list

def make_rating_list(movies):
    value_list = []
    for key in movies:
        value_list.append(movies[key])
    return value_list

def sort_list(list):
    list.sort(reverse=True)
    return list

def sum_list(list):
    sum = 0
    for num in list:
       sum += num
    return sum

def avergae(movies):
   value_list = make_rating_list(movies)
   average = sum_list(value_list) / len(value_list)
   return average

def make_median(movies):
    sorted_list = sort_list(make_rating_list(movies))
    # finds the middle vlaue of the list (for the meidan)
    mid_index = len(sorted_list) // 2 - 1
    median = 0
    # when list is even
    if len(sorted_list) % 2 == 0:
        median = (sorted_list[mid_index] + sorted_list[mid_index+1]) / 2
    # when lst is uneven
    else:
        median = sorted_list[mid_index]
    return median

def best_movie(movies):
    best_key = max(movies, key = movies.get)
    best_val = movies[max(movies, key = movies.get)]
    return best_key, best_val

def worst_movie(movies):
    worst_key = min(movies, key = movies.get)
    worst_val = movies[min(movies, key = movies.get)]
    return worst_key, worst_val

# statistics esten
def print_statistiks(movies):
    movie_list = make_rating_list(movies)
    sorted_list = sort_list(movie_list)
    average = avergae(movies)
    median = make_median(movies)
    best_key, best_val = best_movie(movies)
    worst_key, worst_val = worst_movie(movies)
    print()
    print("The statistics are:")
    print(f"Average of rating: {average:.2f}")
    print(f"The median of rating is: {median}")
    print(f"The best movie is: {best_key} : {best_val}")
    print(f"The worst movie is: {worst_key} : {worst_val}")
    what_to_do(int(print_menu(back_to_menu())), movies)

def update_rating(movies):
    print_movies_and_ratings(movies)
    selected_movie = input("Wich of these movie ratings, you want to update? ")
    new_rating = float(input("What is the new rating?(float) "))
    movies[selected_movie] = new_rating
    what_to_do(int(print_menu(back_to_menu())), movies)

def delete_movie(movies):
    print_movie_list(movies)
    del_movie = input("Wich movie, from this list, you want delete?:")
    del movies[del_movie]
    what_to_do(int(print_menu(back_to_menu())), movies)

def add_movie(movies):
    new_movie = input("Whats the name of the movie?: ")
    rating = float(input("What is its rating?(float): "))
    movies[new_movie] = rating
    what_to_do(int(print_menu(back_to_menu())), movies)

def list_all_movies(movies : dict):
    print_movies_and_ratings(movies)
    what_to_do(int(print_menu(back_to_menu())), movies)

def print_movies_and_ratings(movies):
    print()
    print("********** Al Movies **********")
    for key in movies.keys():
        print(key, movies[key], sep = " : ")

def print_movie_list(movies):
    print()
    print("********** Al Movies **********")
    for key in movies.keys():
        print(key)

def what_to_do(user_input, movies):
    if user_input == 1:
        list_all_movies(movies)
    if user_input == 2:
        add_movie(movies)
    if user_input == 3:
        delete_movie(movies)
    if user_input == 4:
        update_rating(movies)
    if user_input == 5:
        print_statistiks(movies) # testen
    if user_input == 6:
        random_movie(movies)
    if user_input == 7:
        search_movie(movies)
    if user_input == 8:
        movies_sorted(movies)

def back_to_menu():
    return input("\npress Enter to continue")

def print_menu(user_input = ""):
    print("")
    print("Menu:")
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
  # Dictionary to store the movies and the rating
  movies = {
      "The Shawshank Redemption": 9.5,
      "Pulp Fiction": 8.8,
      "The Room": 3.6,
      "The Godfather": 9.2,
      "The Godfather: Part II": 9.0,
      "The Dark Knight": 9.0,
      "12 Angry Men": 8.9,
      "Everything Everywhere All At Once": 8.9,
      "Forrest Gump": 8.8,
      "Star Wars: Episode V": 8.7
  }
  # print_menu gibt 1 - 8 aus, als string
  print("********** My Movies Database **********")
  what_to_do(int(print_menu()), movies)

if __name__ == "__main__":
  main()
