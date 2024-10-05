def remove_punctuation(username):
    new_text = "" # hier wird der neue name gespeichert
    #print(username)
    for char in username:
        #print(char)
        if char in [":", ";", ".", ",", "!", "?"]:
            pass
        else:
            new_text += char
    #print(new_text)
    return new_text


def spaces_to_underlines(text):
    print(text) # überprüfung ob der richtige input in der funktion ist
    new_text = ""
    for char in text:
        #print(char) # wird jeder buchstabe durchgegangen?
        if char == " ":
            print(char, "if") # welcher buchstabe wird hier überprüft
            new_text += "_"
        else:
            print(char, "else") # welcher buchstabe wirdhier überprüft
            new_text += char
    return new_text


def shorten_username(text):
    return text[:9]


def main(username):
    new_username = remove_punctuation(username)
    without_spaces = spaces_to_underlines(new_username)
    print(shorten_username(without_spaces))

if __name__ == "__main__": # __name__ ist eine abrage aus python. __main__ bedeutet, dass das file direckt ausgeführt wird und nicht in eineam anderenf ile ausgeführt wird.
    username = "jonny, smith!"  # We want to transform this to johnny_smi
    main(username)
