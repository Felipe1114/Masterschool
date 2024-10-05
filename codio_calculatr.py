def calculate(text_input):
  text_input = text_input
  text_to_numbers = text_input.split("+")
  result = int(text_to_numbers[0]) + int(text_to_numbers[1])
  return result


print("Welcome to the Python calculator!")
user_input = input("What do you want to calculate? ")
result = calculate(user_input)
print(f"The answer is {result}")