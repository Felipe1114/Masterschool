def is_sum_of_two_primes(number):
  if number % 2 == 1:
    return False
  # hier muss die nächste funktion hin
  for first_num in range(2, number):
    first_num_is_prime = True
    # check if i is a prime
    divisor = 2
    while divisor<first_num:
      if first_num % divisor == 0:
        first_num_is_prime = False
      divisor += 1
    if first_num_is_prime:
      # i is a prime, now check if j=x-i is prime
      sec_num = number - first_num
      if sec_num >= 2:#j must be greater or equal 2 to be prime
        sec_num_is_prime = True
        divisor = 2
        while divisor < sec_num:
          if sec_num % divisor == 0:
            sec_num_is_prime = False
          divisor += 1
        if sec_num_is_prime:
          print(f"The number {number} equals to the sum of {first_num} and {sec_num}")
  return True

def main():
  Number = int(input("Enter a number:"))
  is_sum_of_two_primes(Number)


if __name__ == "__main__":
  main()