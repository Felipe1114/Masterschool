import json
import validade_input as val
CD = val.COMMANDS_DICT


def main():
  """
  extrudes all nececary informations from Json-file.
  hands over informations to the 'main' menu"""
  ship_informations = get_all_variables()
  menu(ship_informations)


#base data functions


def get_json_data(file_path:str):
  """
  hands over the Json-file in the variable 'data'
  """
  with open(file_path, "r") as fileobj:
    data = json.load(fileobj)
  return data


def get_len_of_lst(list) -> int:
  list_len = len(list)
  return list_len


def get_ship_informations_as_lst(ship_lst:list, key_name) -> list:
  """Shipinformations are safed in a dict. The functions can extrude all Ship names,
  or country names, form the dict, in a list.

  Args:
    ship_lst: sip_lst is a list of dict´s. Every dict contains all informations over
    one ship (f.exmpl.: all informations for Queen Mary 2)
    key_name(str): the key for the dict. (f.exmpl: "SHIPNAME")

  Returns:
    list: a list of all vals of one specific key, of all dicts in the ship_lst
  """
  list = []
  for dict in ship_lst:
    list.append(dict[key_name])
  return list


def get_num_of_countries(ship_lst:list, key_name:str="COUNTRY") -> dict:
  """Gets the num of countries form ship_lst.

  Args:
    ship_lst: sip_lst is a list of dict´s. Every dict contains all informations over
    one ship (f.exmpl.: all informations for Queen Mary 2)
    key_name: in this case, key_name is p. default "COUNTRY"

  Returns:
    num_countries: a dictionary of country names(key:str) and their frequency in ship_lst(val:int)

  """
  num_countries = {}
  key_of_shipinformation = key_name
  key = key_of_shipinformation
  for dict in ship_lst:
    if dict[key] not in num_countries:
      num_countries[dict[key]] = 0
    num_countries[dict[key]] += 1
  return num_countries


def get_all_variables() -> dict:
  """Creates all needed variables, out of json-file and packs them in a dict

  Returns:
      Ship_informations(dict): contains all variable names(key) and their values(val)
  """
  ship_data = get_json_data("ships_data.json")
  ship_lst = ship_data["data"]
  total_count = ship_data["totalCount"]
  sum_ships = get_len_of_lst(ship_lst)
  ship_names_lst = get_ship_informations_as_lst(ship_lst, "SHIPNAME")
  num_of_countrys = get_num_of_countries(ship_lst)
  Ship_informations = {}
  Ship_informations["ship_data"] = ship_data
  Ship_informations["ship_lst"] = ship_lst
  Ship_informations["total_count"] = total_count
  Ship_informations["sum_ships"] = sum_ships
  Ship_informations["ship_names_lst"] = ship_names_lst
  Ship_informations["num_of_countrys"] = num_of_countrys
  return Ship_informations


#command functions


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
  len_dict = len(dictionary)
  while True:
    # ist der erste input gut, weitermacen
    # ist der erste input schelcht, neuer input
    try:
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
    except KeyError as e:
      print(f"Not enough Ships in dict:{e}, \n<top_countrys> <= {len_dict}")


def print_dict(dict) -> None:
  for key in dict:
    print(f"{key} : {dict[key]}")


#menu functions


def command_help():
  """prints all possible commands"""
  print("Available commands:\n"
        "help\n"
        "show_countries\n"
        "top_countries <num_countries>\n"
        "exit")


def command_print_country_names(ship_informations:dict):
  """print all country names in sorted order A-Z"""
  country_dict = ship_informations["num_of_countrys"]
  country_names = country_dict.keys()
  print_sorted_list(country_names)


def command_print_top_countries(ship_informations:dict, input_num):
  """print the top X countries, from high to less frequency

  Args:
    ship_informations(dict): a dict of all neccesary ship informations(like num of countries)
  """
  country_dict = ship_informations["num_of_countrys"]
  print_sorted_dict(country_dict, input_num)


def menu(ship_informations):
  """Validades the input, split it up and calls invoked command"""
  while True:
    user_input = input("please type in your command: ")
    input_is_valid = val.validate(user_input)
    if input_is_valid:
      input_list = user_input.split(" ")
      call_commands(ship_informations, input_list)


#command functions


def call_commands(ship_informations, input_list):
  """Calls command, depending on input

  Args:
    ship_informations(dict): a dict of all neccesary ship informations(like num of countries)
    input_list(list): cause I have a command, wich get a num, as input, I splits up the Input to get the input_num
                      the input str = input_list[0], the input num = input_list[1]
  Vars:
    possible_commands(dict):{
      "num_commands" : [
        "top_countries"
      ],
      "basic_commands" : [
        "help",
        "show_countries",
        "exit"
      ]
    }
  """
  bc = "basic_commands"
  nc = "num_commands"
  if input_list[0] == CD[bc][0]:
    command_help()
  elif input_list[0] == CD[bc][1]:
    command_print_country_names(ship_informations)
  elif input_list[0] == CD[bc][2]:
    exit()
  elif input_list[0] == CD[nc][0]:
    try:
      input_num = int(input_list[1])
      command_print_top_countries(ship_informations, input_num)
    except ValueError as e:
      print(f"<num countriea> must be a number: {e}")

if __name__ == "__main__":
  main()