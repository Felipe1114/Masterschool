ROME_AND_JULIET_TEXT = PLAY

def print_most_words(dictionary : dict):
    for key in dictionary:
        print(f"{key} : {dictionary[key]}")

def find_most_words(dictionary : dict):
    '''
    creates a new dict (fifty_most_words)
    copys the dict 'dictionary', so the original dict is not touched
    gets the most fifty values from the dict 'dic_copy' and deletes the key from this value,
    so the second highest val is the new highest val
    '''
    dic_most_words = {}
    dic_copy = dictionary.copy()
    highest_key = ""
    while len(dic_most_words) < 50:
        highest_val = 0
        for key, val in dic_copy.items():
            if val > highest_val:
                highest_val = val
                highest_key = key
        del dic_copy[highest_key]
        dic_most_words[highest_key] = highest_val
    return dic_most_words

def make_dic_r_and_j(string : str):
    '''
   makes a list form the string 'string_without_special_chars'
   makes a dic from the list 'list_r_and_j'
    '''
    list_r_and_j = string.lower().split(" ")
    dic_r_and_j = {}
    for word in list_r_and_j:
        if word not in dic_r_and_j:
            dic_r_and_j[word] = 0
        dic_r_and_j[word] += 1
    return dic_r_and_j


def removoe_spec_characters():
    '''
    replaces all special characters in the string with empty space.
    '''
    lst_special_char = ['\n', '.', '\\', '[', ']', '_', ',', ';', '?', '!', ':', ]
    str_without_spec_char = PLAY
    for char in lst_special_char :
        str_without_spec_char = str_without_spec_char.replace(char, "")
    return str_without_spec_char


def main():
    '''
    first: List with all Special characters, wich should be removed from the text.
    second: dic_words contains a dictionary with all words from the text, without special characters
    third: prints the most fifty words form the dict 'dic_most_words'
    '''
    str_without_spec_char = removoe_spec_characters()
    dic_r_and_j = make_dic_r_and_j(str_without_spec_char)
    dic_most_words = find_most_words(dic_r_and_j)
    print_most_words(dic_most_words)


if __name__ == "__main__":
    main()
