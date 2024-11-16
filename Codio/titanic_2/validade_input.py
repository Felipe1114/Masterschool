COMMANDS_DICT = {
  "num_commands" : [
    "top_countries"
  ],
  "basic_commands" : [
    "help",
    "show_countries",
    "exit"
  ]
}


def main():
  validate(input())


def create_command_list():
  """gives back a list of all possible commands

  Returns:
    possible_commands(dict): all possible commands in a list
    """
  CD = COMMANDS_DICT
  nc = "num_commands"
  bc = "basic_commands"
  possible_commands = CD[nc]
  for command in CD[bc]:
    possible_commands.append(command)
  return possible_commands


def split_input(input):
  """splits input and looks for wrong input

  Args:
    input(str): given input from user
  """
  input_list = input.split(" ")
  possible_commands = create_command_list()
  if len(input_list) > 2:
    raise ValueError("Unconform Input. Input must have '_' as empty space.\n"
                     "If you want write a number, let an empty space between the text and the number.\n"
                     "for example: 'top_countries 5' or 'help'")
  if input_list[0] not in possible_commands:
    raise TypeError("Input must be in possible commands.\n"
                     "Possible Commands:\n"
                     "help\n"
                     "show_countries\n"
                     "exit\n"
                     "top_countries <num_countries>")

  if len(input_list) == 2:
    try:
      input_number = int(input_list[1])
    except ValueError as e:
      print(e)


def validate(user_input="None"):
  """
  splits up input and tests variable cases,
  if no Error is raised validate returns 'True'.

  Args:
    user_input(str): the input from user
  """
  try:
    split_input(user_input)
    return True
  except (ValueError, TypeError) as e:
    print(e)
    return False



if __name__ == "__main__":
  main()