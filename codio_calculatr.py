OPERATOR_LIST = ["+", "-", "*", "/", "~"]

def how_many_calculations():
  input_for_times_to_calculate = input("How many calculations do you want to do? ")
  for i in range(int(input_for_times_to_calculate)):
    find_operator()

def find_operator():
  calculation = input("What do you want to calculate? ")
  operator_index = get_operator_index(calculation)
  numbers = get_numbers(calculation, operator_index)
  math_functions = [addition(numbers), subtraction(numbers), multiplication(numbers), division(numbers), tildation(numbers)]
  operator = define_operator(calculation, operator_index)
  print(math_functions[operator])

def define_operator(calculation, operator_index):
  return OPERATOR_LIST.index(calculation[operator_index])

def get_numbers(calculation, index):
  return [calculation[:index], calculation[index + 1:]]

def get_operator_index(calculation):
  for index in range(len(calculation)):
    if not calculation[index].isalnum():
      return index

def addition(numbers):
  result = int(numbers[0]) + int(numbers[1])
  return(f"The answer is {result}")

def subtraction(numbers):
  result = int(numbers[0]) - int(numbers[1])
  return(f"The answer is {result}")

def multiplication(numbers):
  result = int(numbers[0]) * int(numbers[1])
  return(f"The answer is {result}")

def division(numbers):
  result = int(numbers[0]) / int(numbers[1])
  return(f"The answer is {result}")

def tildation(numbers):
  result_modolo = int(numbers[0]) % int(numbers[1])
  result_floordivision = int(numbers[0]) // int(numbers[1])
  return(f"The answer is {result_floordivision} \nThe remainder is {result_modolo}")

def main():
  print("Welcome to the Python calculator!")
  how_many_calculations()

if __name__ == "__main__":
  main()

