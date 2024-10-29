'''def until_stop(list): # gibt liste bis zu STOP aus
    sublist = []
    i = 0
    while True:
        if list[i] == "STOP":
            break
        sublist.append(list[i])
        if i == len(list) - 1:
            break
        i += 1
    print(sublist)

until_stop(["hey", "joe", "meow", "test"])
'''
from itertools import count


# gibt die länge eines strings zurück und die anzahl der wörter
# anzahl der wörter: einen split benutzten
def get_input():
    string = input("Type in, an string: ")
    return string

def lenght_of_string(string):
    lenght = len(list(string))
    return lenght

def count_words(string):
    words_in_list = string.split("\t")
    word_count = len(words_in_list)
    return word_count

def endless_loop():
    while True:
        string = get_input()
        if string == "Quit":
            break
        string_lenght = lenght_of_string(string)
        num_of_words = count_words(string)
        print(f"this String has {string_lenght} letters and {num_of_words} words")


def main():
    endless_loop()

if __name__ == "__main__":
  main()
