def find_double_pair_of_primes(first_num, sec_num):
  """catches evry prime number pair in a dict.
  compares the values from the dict with the next prime number.
  If the last created value is the key of the current value
  the search for prime pairs will end
  cause in evry case, except if is True, we will have an KeyError
  an except replaces the else
  Args:
    first_num(int): first num of the current prime pair
    sec_num(int): sec num of the current prime pair

  Returns:
    True(Bool): if the Return is True, the loop for seraching for prime pairs, will end
  """
  try:
    if first_num == dict_prime_pairs[sec_num]:
      return True
  except KeyError:
    dict_prime_pairs[first_num] = sec_num
    print(dict_prime_pairs)
    return False


def print_result(first_num, number, sec_num, sec_num_is_prime):
  """The funktion takes first_num and sec_num and prints the pair,
  if sec_num is prime.
  But, if all_pairs_found is true (so the programm would begin to print
  all pairs again) the loop ends

  Args:
    first_num(int): first number of a possible prime pair
    sec_num(intI): sec number of a possible prime pair
    number(int): the number we´re checking for prime pairs
    sec_num_is_prime(bool): says, if sec_num is a prime num

  Returns:
      all_pairs_found(bool): says, if all prime paris are found
  """
  if sec_num_is_prime:
    all_pairs_found = find_double_pair_of_primes(first_num, sec_num)
    if all_pairs_found:
      return all_pairs_found
    print(f"The number {number} equals to the sum of {first_num} and {sec_num}")
  else:
    all_pairs_found = False
  return all_pairs_found


def if_sec_num_greater_equal_two(first_num, number, sec_num):
  """looks, if sec_num has all requirements for a prime num
  is that the case, sec_num will be profed if its realy a prime num
  than first_num and sec_num will be printed

  Args:
    first_num(int): first number of a possible prime pair
    sec_num(intI): sec number of a possible prime pair
    number(int): the number we´re checking for prime pairs

  Returns:
          all_pairs_found(bool): says, if all prime paris are found
  """
  all_pairs_found = False
  if sec_num >= 2:
    sec_num_is_prime = validate_prime(sec_num)
    all_pairs_found = print_result(first_num, number, sec_num, sec_num_is_prime)
  return all_pairs_found


def is_first_num_prime(first_num, first_num_is_prime, number):
  """checks, if first_num is a prime num

  Args:
    first_num(int): first number of a possible prime pair
    first_num_is_prime(bool): is first_num a prime num?
    number(int): the number we´re checking for prime pairs

  """
  all_pairs_found = False
  if first_num_is_prime:
    sec_num = number - first_num
    all_pairs_found = if_sec_num_greater_equal_two(first_num, number, sec_num)
  return all_pairs_found


def validate_prime(num_to_check) -> bool:
  """checks, if a number is a prime number

  Args:
    num_to_check(int): the number to check

  Returns:
    num_is_prime(bool): is num_to_check a prime num?
  """
  num_is_prime = True
  divisor = 2
  while divisor < num_to_check:
    if num_to_check % divisor == 0:
      num_is_prime = False
    divisor += 1
  return num_is_prime


def find_first_num(number) -> bool:
  """searches for all possible prime numbers in a range from 2 to number
  if all pairs of prime numbers are found, the loop ends

  Args:
        number(int): the number we´re checking for prime pairs
  """
  for first_num in range(2, number):
    first_num_is_prime = validate_prime(first_num)
    all_pairs_found = is_first_num_prime(first_num, first_num_is_prime, number)
    if all_pairs_found == True:
      break


def is_sum_of_two_primes(number):
  """gets a number(int) and checks if the number is even
  if True: find_first_num is called

  Args:
    number(int) a number in his range, we want to find all existing prime numbers
  """
  if number % 2 != 1:
    find_first_num(number)



def main():
  """Takes an input from User and calls "is_sum_of_tow_primes(input)"
  If input is not an int, an error is risen and the user is asked for a new input
  """
  while True:
    try:
      number = int(input("Enter a number: "))
      break
    except ValueError as e:
      print(e)
  is_sum_of_two_primes(number)


dict_prime_pairs = {}
if __name__ == "__main__":
  main()