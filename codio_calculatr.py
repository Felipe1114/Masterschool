# the mainfunction:
def calculate(text_input):
  for calculation in range(int(text_input)): # how many times the user want to calculate
    # because we get from the Input a string, we need to change it, into an Integer with "int()"
    formular_input = input("What do you want to calculate? ") # her comes the input like: 32+43
    operator_list = ["+", "-", "*", "/", "~"] # important to defince, wich calculation should be made
    # operator        0    1    2    3    4
    # indicies:      ^^^^^^^^^^^^^^^^^^^^^^^^

    #---------------------------------------------
    for operator in operator_list:                        # here we search for the operator thrue a loop,
      operator_index = formular_input.find(operator)      # where we are going thrue the list of possible operators
      list_index = operator_list.index(operator)          # and when we find him (the operator), the find() method
      if operator_index != -1:                            # will give us an positive number
        here_happens_the_math(formular_input, list_index) # the list_index is for making the "right" math
        #^^^^^^^^^^^^^^^^^^^^^
        # when we geht our positive number, we are calling the function, where the math is happening

    #----------------------------------------------
#--------------------------------------------------------#
# here is happening the math:
def here_happens_the_math(formular_input, list_index):
  # the indicies are referenced in the list_index; 0 = +, 1 = -; 2 = *; 3 = /; 4 = ~
  # so, if our operator_index is 3, we now, that the user want to divide
  if list_index == 0: # addition
    addition(formular_input)
  if list_index == 1: # substraktion
    subtraction(formular_input)
  if list_index == 2: # multiplikation
    multiplication(formular_input)
  if list_index == 3: # division
    division(formular_input)
  if list_index == 4: # tildation (tilde)
    tildation(formular_input)
#--------------------------------------------------------#
# here are the functions for the mathematical operations:
def addition(formular_input):
  print("you are in addition")
  text_to_numbers = formular_input.split("+")                 # splits the string into a list of two numbers
  result = int(text_to_numbers[0]) + int(text_to_numbers[1])
  print(f"The answer is {result}")
  #---------------------------------
def subtraction(formular_input):
  print("you are in subraction")
  text_to_numbers = formular_input.split("-")                 # splits the string into a list of two numbers
  result = int(text_to_numbers[0]) - int(text_to_numbers[1])
  print(f"The answer is {result}")
  #---------------------------------
def multiplication(formular_input):
  print("you are in multiplication")
  text_to_numbers = formular_input.split("*")                 # splits the string into a list of two numbers
  result = int(text_to_numbers[0]) * int(text_to_numbers[1])
  print(f"The answer is {result}")
  #---------------------------------
def division(formular_input):
  print("you are in division")
  text_to_numbers = formular_input.split("/")                 # splits the string into a list of two numbers
  result = int(text_to_numbers[0]) / int(text_to_numbers[1])
  print(f"The answer is {result}")
  #---------------------------------
def tildation(formular_input):
  print("you are in tildation")
  text_to_numbers = formular_input.split("~")                 # splits the string into a list of two numbers
  result_modolo = int(text_to_numbers[0]) % int(text_to_numbers[1])
  result_floordivision = int(text_to_numbers[0]) // int(text_to_numbers[1])
  print("The answer is ", result_floordivision, "\n", "The remainder is ", result_modolo, sep="")
  # ---------------------------------
#--------------------------------------------------------#
#here comes the code:
print("Welcome to the Python calculator!")
user_input = input("How many calculations do you want to do? ") # returns a number in a string
calculate(user_input)
