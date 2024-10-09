# the mainfunction:
def how_many_calculations():
  input_for_times_to_calculate = input("How many calculations do you want to do? ")
  for i in range(int(input_for_times_to_calculate)):
    find_operator()
   
def find_operator():
  input_for_calculation = input("What do you want to calculate? ")
  operator_list = ["+", "-", "*", "/", "~"]
  for i in range(len(operator_list)):
    if operator_list[i] in input_for_calculation:
      list_index = i
      input_for_calculation_splitted_up = input_for_calculation.split(operator_list[i])
      here_happens_the_math(list_index, input_for_calculation_splitted_up)
      
def here_happens_the_math(list_index, input_for_calculation_splitted_up):
  if list_index == 0: 
    addition(input_for_calculation_splitted_up)
  elif list_index == 1: 
    subtraction(input_for_calculation_splitted_up)
  elif list_index == 2: 
    multiplication(input_for_calculation_splitted_up)
  elif list_index == 3: 
    division(input_for_calculation_splitted_up)
  else: 
    tildation(input_for_calculation_splitted_up)

def addition(input_for_calculation_splitted_up):
  result = int(input_for_calculation_splitted_up[0]) + int(input_for_calculation_splitted_up[1])
  print(f"The answer is {result}")

def subtraction(input_for_calculation_splitted_up):
  result = int(input_for_calculation_splitted_up[0]) - int(input_for_calculation_splitted_up[1])
  print(f"The answer is {result}")

def multiplication(input_for_calculation_splitted_up):
  result = int(input_for_calculation_splitted_up[0]) * int(input_for_calculation_splitted_up[1])
  print(f"The answer is {result}")

def division(input_for_calculation_splitted_up):
  result = int(input_for_calculation_splitted_up[0]) / int(input_for_calculation_splitted_up[1])
  print(f"The answer is {result}")

def tildation(input_for_calculation_splitted_up):
  result_modolo = int(input_for_calculation_splitted_up[0]) % int(input_for_calculation_splitted_up[1])
  result_floordivision = int(input_for_calculation_splitted_up[0]) // int(input_for_calculation_splitted_up[1])
  print(f"The answer is {result_floordivision} \nThe remainder is {result_modolo}")

def main():
  print("Welcome to the Python calculator!")
  how_many_calculations()

if __name__ == "__main__":
  main()

