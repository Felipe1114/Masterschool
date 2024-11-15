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
  print("before validade")
  validade(input())
  print("after validade")


def create_command_list():
  CD = COMMANDS_DICT
  nc = "num_commands"
  bc = "basic_commands"
  possible_commands = CD[nc]
  for command in CD[bc]:
    possible_commands.append(command)
  return possible_commands


def split_input(input):
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


def validade(user_input="None"):
  """
  splites up input and tests variable cases,
  if no Error is raised validade returns 'True'.
  """
  try:
    split_input(user_input)
    return True
  except (ValueError, TypeError) as e:
    print(e)
    return False



if __name__ == "__main__":
  main()