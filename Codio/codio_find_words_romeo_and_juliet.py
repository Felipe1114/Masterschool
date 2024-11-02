from Codio.romeo_and_juliet import PLAY
ROME_AND_JULIET_TEXT = PLAY

# gives a list without special characters; but all lettes are a single element in the list
def text_to_list(remove_list):
    filtred_list = []
    for index in range(len(ROME_AND_JULIET_TEXT)):
        if ROME_AND_JULIET_TEXT[index] not in remove_list:
            filtred_list.append(ROME_AND_JULIET_TEXT[index])
    print(filtred_list)
    return filtred_list

# makes a full text from the filtred list
def list_to_text(text_to_list):
    filtred_text = "".join(text_to_list)
    print(filtred_text)
    return filtred_text

# gives a list of all words from the filtred_text
def make_alpha_list(filtred_text):
    word_list = filtred_text.split(" ")
    print(word_list)
    return word_list

# counts all words in the filtred_list and puts them into a dictionary
def create_dictionary(filterd_list):
    julites_dictionary = {}
    for word in filterd_list:
        if word not in julites_dictionary:
            julites_dictionary[word] = 0
        julites_dictionary[word] += 1
    return julites_dictionary

# finds the 50 keys with the hightes values
def find_50_highest_vales(juliets_dcitionary):
    fifty_most_wors = {}
    highest_key = ""
    while len(fifty_most_wors) < 50:
        highest_num = 0
        for key, val in juliets_dcitionary.items():
            if val > highest_num:
                highest_num = val
                highest_key = key
        del juliets_dcitionary[highest_key]
        fifty_most_wors[highest_key] = highest_num
    return fifty_most_wors

def print_words(most_words):
    for key in most_words:
        print(f"{key} : {most_words[key]}")

def main():
    spechial_character_list = ['\n', '.', '\\', '[', ']', '_', ',', ';', '?', '!', ':', ]
    filtred_list = make_alpha_list(list_to_text(text_to_list(spechial_character_list)))
    juliets_dcitionary = create_dictionary(filtred_list)
    print_words(find_50_highest_vales(juliets_dcitionary))

if __name__ == "__main__":
    main()
