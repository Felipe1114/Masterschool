import json

from six import print_

# basic interactions
'''with open("ships_data.json", "r") as fileobj:
    data = json.load(fileobj)

with open("ships_data_copy.json", "w") as fileobj:
    json.dump(data, fileobj, indent=4 )'''


def main():
    """Num of ships(int):
    All Names of ships(list):
    All countries of ships, without duplicates(dict, key = shipname, val = countries(list)
    """
    file_path = "ships_data.json"
    json_data = get_ship_data(file_path)
    ship_lst = json_data["data"]
    total_count = json_data["totalCount"]
    num_ships = get_num_ships(ship_lst)
    num_ships_dict = find_ship_names(ship_lst)
    ship_names = get_ship_names(ship_lst) #gibt zwei mal das schiff "A"
    num_of_country = find_countrys(ship_lst)
    list_country_names = num_of_country.keys()
    printX_popular_countrya(num_of_country)



#======================== base data funktions

def get_ship_data(file_path:str) -> list:
    with open(file_path, "r") as fileobj:
        data = json.load(fileobj)
    return data


def get_num_ships(ship_data:list) -> int:
    num_ships = len(ship_data)
    return num_ships


def get_ship_names(ship_lst:list) -> list:
    ship_names = []
    for dict in ship_lst:
        ship_names.append(dict["SHIPNAME"])
    return ship_names


def find_countrys(ship_lst:list):
    countrys = {}
    key_for_countrys = "COUNTRY"
    key = key_for_countrys
    for dict in ship_lst:
        if dict[key] not in countrys:
            countrys[dict[key]] = 0
        countrys[dict[key]] += 1
    return countrys


def find_ship_names(ship_lst:list):
    ships = {}
    key_for_shipnames = "SHIPNAME"
    key = key_for_shipnames
    for dict in ship_lst:
        if dict[key] not in ships:
            ships[dict[key]] = 0
        ships[dict[key]] += 1
    return ships

#====================command funktions
def print_ship_names(ship_names:list) -> None:
    print("===All ship names===\n")
    string_of_ship_names = ""
    ship_names.sort()
    for name in ship_names:
        string_of_ship_names = string_of_ship_names + name + "\n"
    print(string_of_ship_names)

def printX_popular_countrya(num_countrys:dict) -> None:
    """try: einfügen
    maximale anzahl an schiffen noch einfügen (input darf nicht größer sein,
    als anzal der schiffe)

    """
    input = get_list_lenght()
    num_ships_copy = num_countrys.copy()
    ranked_ships = {}
    for i in range(input):
        highest_val = 0
        highest_key = ""
        for key in num_ships_copy:
            if num_ships_copy[key] > highest_val:
                highest_val = num_ships_copy[key]
                highest_key = key
        ranked_ships[highest_key] = highest_val
        num_ships_copy.pop(highest_key)
    print_keys_and_vals(ranked_ships)


def print_keys_and_vals(dict):
    for key in dict:
        print(f"{key} : {dict[key]}")


def get_list_lenght() -> int:
    while True:
        try:
            range = int(input("How long should the list be?(int): "))
            break
        except ValueError as e:
            print(f"Not an integer: {e}, type an integer")
    return range


if __name__ == "__main__":
    main()