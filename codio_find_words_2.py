from romeo_and_juliet import PLAY
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
    play1 = PLAY.replace('.', "")
    play2 = play1.replace('\\', "")
    play3 = play2.replace('[', "")
    play4 = play3.replace(']', "")
    play5 = play4.replace('_', "")
    play6 = play5.replace(',', "")
    play7 = play6.replace(';', "")
    play8 = play7.replace('?', "")
    play9 = play8.replace('!', "")
    play10 = play9.replace(':', "")
    play11 = play10.replace('’', "")
    play12 = play11.replace('\n', "")
    return play12

def main():
    '''
    first: List with all Special characters, wich should be removed from the text.
    second: dic_words contains a dictionary with all words from the text, without special characters
    third: prints the most fifty words form the dict 'dic_most_words'
    '''
    string_without_special_chars = removoe_spec_characters()
    dic_r_and_j = make_dic_r_and_j(string_without_special_chars)
    dic_most_words = find_most_words(dic_r_and_j)
    print_most_words(dic_most_words)


if __name__ == "__main__":
    main()
