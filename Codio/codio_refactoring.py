def print_result(first_num, number, sec_num, sec_num_is_prime):
  if sec_num_is_prime:
    print(f"The number {number} equals to the sum of {first_num} and {sec_num}")


def if_sec_num_greater_equal_two(first_num, number, sec_num):
  if sec_num >= 2:  # j must be greater or equal 2 to be prime
    sec_num_is_prime = validate_prime(sec_num)
    print_result(first_num, number, sec_num, sec_num_is_prime)


def is_first_num_prime(first_num, first_num_is_prime, number):
  if first_num_is_prime:
    sec_num = number - first_num
    if_sec_num_greater_equal_two(first_num, number, sec_num)


def validate_prime(num_to_check) -> bool:
  """

  """
  num_is_prime = True
  divisor = 2
  while divisor < num_to_check:
    if num_to_check % divisor == 0:
      num_is_prime = False
    divisor += 1
  return num_is_prime


def find_first_num(number) -> bool:
  """

  """
  for first_num in range(2, number):
    first_num_is_prime = validate_prime(first_num)
    is_first_num_prime(first_num, first_num_is_prime, number)
  return True


def is_sum_of_two_primes(number):
  """gets a number(int) and checks if the number is odd
  Is the number even: find_first_num is called

  Args:
    number(int) a number in his range, we want to find all existing prime numbers
  """
  if number % 2 == 1:
    return False
  else:
    find_first_num(number)


def main():
  Number = int(input("Enter a number:"))
  is_sum_of_two_primes(Number)


if __name__ == "__main__":
  main()