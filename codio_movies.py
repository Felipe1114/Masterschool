'''  Aufgaben:
  x Menu
  x nach auswahl wieder zurück zu menu
  x Alle Filme auflisten
  x einen Film hinzufügen
  x einen film löschen
  x einen film updaten (die wertung ändern)
  x die statistiken anzeigen:
  x - durchschnitt, median, bester, schlechtester
  einen zufälligen film printen
  nach einem film suchen (case insensitiv)
  filme nach rating anzeigen
  '''
def make_rating_list(movies):
    value_list = []
    for key in movies:
        value_list.append(movies[key])
    return value_list

def sort_list(list):
    sorted_list = list.sort()
    return sorted_list

def sum_list(list):
    sum = 0
    for num in list:
       sum += num
    return sum

def avergae(movies):
   value_list = make_rating_list(movies)
   average = sum_list(value_list) / len(value_list)
   return average

def median(movies):
    sorted_list = sort_list(make_rating_list(movies))
    # findet den mittleren wert der sortierten liste (für den median)
    mid_index = len(list) / 2 - 1
    median = 0
    # wenn liste gerade ist
    if len(sorted_list) % 2 == 0:
        median = (sorted_list[mid_index] + sorted_list[mid_index+1]) / 2
    # wenn liste ungerade ist
    else:
        median = sorted_list[mid_index]
    return median

def best(sorted_list):
    best = sorted_list[0]
    return best

def worst(sorted_list):
    worst = sorted_list[-1]
    return worst

def print_statistiks(movies):
    movie_list = make_rating_list(movies)
    sorted_list = sort_list(movie_list)
    average = avergae(movies)
    median = median(movies)
    best_movie = best(sorted_list)
    worst_movie = worst(sorted_list)
    print("The statistics are:")
    print(f"Average of rating: {average}")
    print(f"The median of rating is: {median}")
    print(f"The best movie is: {best_movie}")
    print(f"The worst movie is: {worst_movie}")

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
    print_movie_list(movies)
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
    # hier test prints einfügen
    #===============================
    print(movies)
    print(len(movies))
    #===============================
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
        # random movie
        pass
    if user_input == 7:
        # search movie
        pass
    if user_input == 8:
        # movies sorted by rating
        pass

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
