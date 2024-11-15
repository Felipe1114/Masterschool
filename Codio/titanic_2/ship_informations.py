import json
# basic interactions
'''with open("ships_data.json", "r") as fileobj:
    data = json.load(fileobj)

with open("ships_data_copy.json", "w") as fileobj:
    json.dump(data, fileobj, indent=4 )'''


def main():
    """
    Vars:
        ship_lst: all ship names
        sum_ships(int): sum of all ships
        ship_names_lst: all names of ships in Json file
        num_of_countrys(dict): dict of countrys, key=country name, val=sum of country


    """
    file_path = "ships_data.json"
    json_data = get_json_data(file_path)
    ship_lst = json_data["data"]
    total_count = json_data["totalCount"] # weiß noch nicht wfür das hier gut ist
    sum_ships = get_len_of_lst(ship_lst)
    ship_names_lst = get_ship_informations_as_lst(ship_lst, "SHIPNAME") #gibt zwei mal das schiff "A"
    num_of_countrys = get_ship_informations_as_dict(ship_lst, "COUNTRY")


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

#====================command funktions


def print_list(list) -> None:
    print("===All ship names===\n")
    concatenated_str = ""
    list.sort()
    for sub_string in list:
        concatenated_str = concatenated_str + sub_string + "\n"
    print(concatenated_str)


def sort_and_print_dict(given_dict:dict) -> None:
    """prints the best key/val combination, of a given dict.
    takes an int form user, for the <num of best key/val>
    sorts the given dict, than prints it

    Args:
        given_dict(dict)
    """
    # try: einfügen, max anzahl an iteratiojns = len(dictionary)
    len_sorted_dict = get_int_from_user("dictionary")
    dict_copy = given_dict.copy()
    sorted_dict = sort_dict(len_sorted_dict, dict_copy)
    print_keys_and_vals(sorted_dict)


def sort_dict(len_soted_dict:int, dictionary:dict) -> dict:
    """Sorts the keys and values of a dict in a new dict, from best to less.
    Only works, if values:int
    
    Args:
        len_soted_dict(int): defines, how long the sorted dict is; 
        for the ten best vals num_of_iteration = 10;
        never should be higher, than the len, of Arg:dictionary
        dictionary(dict): the dict, wich will be sorted
    
    Returns:
        sorted_dict(dict): a dict, with the sorted keys and vals of Arg(dictionary)
    """
    # try: einfügen, max anzahl an iteratiojns = len(dictionary)
    sorted_dict = {}
    for i in range(len_soted_dict):
        best_val = 0
        best_key = ""
        for key in dictionary:
            if dictionary[key] > best_val:
                best_val = dictionary[key]
                best_key = key
        sorted_dict[best_key] = best_val
        dictionary.pop(best_key)
    return sorted_dict


def print_keys_and_vals(dict) -> None:
    for key in dict:
        print(f"{key} : {dict[key]}")


def get_int_from_user(data_structur:str) -> int:
    """takes an int from user; will be used for the range, in a for loop

    Args:
        data_structur(str): Name of an iterable data type(list, dict)

    Returns:
        range(int): will be used for the range, in a for loop
    """
    while True:
        try:
            range = int(input(f"How long should the {data_structur} be?(int): "))
            break
        except ValueError as e:
            print(f"Not an integer: {e}, type an integer")
    return range


#====================== menu functions
#command help:

#command show_countrys

#command top_countries <num_countries>


if __name__ == "__main__":
    main()