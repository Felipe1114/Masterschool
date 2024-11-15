import json
# basic interactions
'''with open("ships_data.json", "r") as fileobj:
    data = json.load(fileobj)

with open("ships_data_copy.json", "w") as fileobj:
    json.dump(data, fileobj, indent=4 )'''

"""
programm aufbau:
programm wartet immer auf input (leeres input statement?)
nach jeder funktion geht es immer wieder zur menu funktion
"""

def main():
    """Calls menu()
    """
    ship_informations = get_all_variables()
    while True:
        menu(ship_informations)



#======================== base data funktions


def get_json_data(file_path:str):
    with open(file_path, "r") as fileobj:
        data = json.load(fileobj)
    return data


def get_len_of_lst(list) -> int:
    list_len = len(list)
    return list_len


def get_ship_informations_as_lst(ship_lst:list, key_name) -> list:
    list = []
    for dict in ship_lst:
        list.append(dict[key_name])
    return list


def get_ship_informations_as_dict(ship_lst:list, key_name) -> dict:
    dictionary = {}
    key_of_shipinformation = key_name
    key = key_of_shipinformation
    for dict in ship_lst:
        if dict[key] not in dictionary:
            dictionary[dict[key]] = 0
        dictionary[dict[key]] += 1
    return dictionary


def get_all_variables() -> dict:
    """Creates all needed variables, out of json-file

    Returns:
        all_variables(dict): contains all variables
    """
    ship_data = get_json_data("ships_data.json")
    ship_lst = ship_data["data"]
    total_count = ship_data["totalCount"]
    sum_ships = get_len_of_lst(ship_lst)
    ship_names_lst = get_ship_informations_as_lst(ship_lst, "SHIPNAME")
    num_of_countrys = get_ship_informations_as_dict(ship_lst, "COUNTRY")
    all_variables = {}
    all_variables["ship_data"] = ship_data
    all_variables["ship_lst"] = ship_lst
    all_variables["total_count"] = total_count
    all_variables["sum_ships"] = sum_ships
    all_variables["ship_names_lst"] = ship_names_lst
    all_variables["num_of_countrys"] = num_of_countrys
    return all_variables


#====================command funktions


def print_sorted_list(list:list) -> None:
    concatenated_str = ""
    sorted_list = sorted(list)
    #list.sort())
    for sub_string in sorted_list:
        concatenated_str = concatenated_str + sub_string + "\n"
    print(concatenated_str)


def print_sorted_dict(given_dict:dict, range) -> None:
    """prints the best key/val combination, of a given dict.
    takes an int form user, for the <num of best key/val>
    sorts the given dict, than prints it

    Args:
        given_dict(dict)
    """
    # try: einfügen, max anzahl an iteratiojns = len(dictionary)

    dict_copy = given_dict.copy()
    sorted_dict = sort_dict(range, dict_copy)
    print_dict(sorted_dict)


def sort_dict(len_new_dict:int, dictionary:dict) -> dict:
    """Sorts the keys and values of a dict in a new dict, from best to less.
    Only works, if values:int
    
    Args:
        len_new_dict(int): defines, how long the sorted dict is;
        for the ten best vals num_of_iteration = 10;
        never should be higher, than the len, of Arg:dictionary
        dictionary(dict): the dict, wich will be sorted
    
    Returns:
        sorted_dict(dict): a dict, with the sorted keys and vals of Arg(dictionary)
    """
    # try: einfügen, max anzahl an iteratiojns = len(dictionary)
    sorted_dict = {}
    for i in range(len_new_dict):
        best_val = 0
        best_key = ""
        for key in dictionary:
            if dictionary[key] > best_val:
                best_val = dictionary[key]
                best_key = key
        sorted_dict[best_key] = best_val
        dictionary.pop(best_key)
    return sorted_dict


def print_dict(dict) -> None:
    for key in dict:
        print(f"{key} : {dict[key]}")

#===============input_functions


def get_input() -> tuple:
    """takes user input
    """
    user_input = input()
    command, range = slice_input(user_input)
    return command, range

# index error. wenn kein integer am ende, gibt es beim split(" ") nur ein element in der list
# problem beheben
def slice_input(input):

    splited_input = input.split(" ")
    try:
        command = splited_input[0]
        range = int(splited_input[1])
    except IndexError:
        range = None
    finally:
        return command, range


#====================== menu functions
def command_help():
    print("Available commands:\nhelp\nshow_countries\ntop_countries <num_countries>")


def command_print_country_names(ship_informations:dict):
    country_dict = ship_informations["num_of_countrys"]
    country_names = country_dict.keys()
    print_sorted_list(country_names)


def command_print_top_countries(ship_informations:dict, range):
    country_dict = ship_informations["num_of_countrys"]
    print_sorted_dict(country_dict, range)


def menu(ship_informations):
    command, range = get_input()
    if range == None:
        ohter_commands(ship_informations, command)
    if type(range) == int:
        if command == "top_countries":
            command_print_top_countries(ship_informations, range)


def ohter_commands(ship_informations, command):
    if command == "show_countries":
        command_print_country_names(ship_informations)
    elif command == "help":
        command_help()
    elif command == "exit":
        exit()


if __name__ == "__main__":
    main()