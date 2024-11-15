import json
import validade_input as val
CD = val.COMMANDS_DICT


def main():
  """
  gets all necesarry informations in a dict, than calls menu
  """
  ship_informations = get_all_variables()
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


#====================== menu functions


def command_help():
  print("Available commands:\n"
        "help\n"
        "show_countries\n"
        "top_countries <num_countries>\n"
        "exit")


def command_print_country_names(ship_informations:dict):
  country_dict = ship_informations["num_of_countrys"]
  country_names = country_dict.keys()
  print_sorted_list(country_names)


def command_print_top_countries(ship_informations:dict, input_num):
  country_dict = ship_informations["num_of_countrys"]
  print_sorted_dict(country_dict, input_num)


def menu(ship_informations):
  while True:
    user_input = input()
    input_is_valid = val.validade(user_input)
    if input_is_valid:
      input_list = user_input.split(" ")
      call_commands(ship_informations, input_list)

#=============== test funktions for excepctions
def validade_test():
  try:
    user_input = test(int(input()))
    if user_input:
      print(f"User inpute = {user_input}")
  except ValueError as e:
    print(e)


def test(user_input):
  if user_input == 5:
    return True
  if user_input == 6:
    raise ValueError("Value Error. keine 6en erlaubt!")

#================= call command




def call_commands(ship_informations, input_list):
  """

  Vars:
    possible_commands =
    {
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