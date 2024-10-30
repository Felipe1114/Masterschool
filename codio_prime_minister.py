def make_parameters(range_list):
    prime_numbers = []
    is_two_in_range(range_list, prime_numbers)
    odd_numbers = get_all_odd_numbers(range_list)
    middle_index = divide_len_odd_numbers(odd_numbers)
    list_divider = split_odd_numbers(odd_numbers, middle_index)
    iterate_thrue_odd_numbers(odd_numbers, list_divider, prime_numbers)

def get_range():
    range_start = int(input("Enter start range: "))
    range_end = int(input("Enter end range: "))
    range_list = [range_start, range_end]
    return range_list

def divide_len_odd_numbers(odd_numbers):
    return len(odd_numbers) // 2 + 2

def split_odd_numbers(odd_numbers, middle_index):
    return odd_numbers[:middle_index]

def get_all_odd_numbers(range_list):
    odd_numbers = []
    for i in range(range_list[0], range_list[1]):
        if i % 2 != 0: odd_numbers.append(i)
    is_one_in_list(odd_numbers)
    return odd_numbers

def iterate_thrue_odd_numbers(odd_numbers, list_divider, prime_numbers):
    for index_numbers in range(len(odd_numbers)):
        check_list = []
        for index_divider in range(len(list_divider)):
            if odd_numbers[index_numbers] == list_divider[index_divider]:
                #print("this is printed, wehn number and divider are equal: \n", odd_numbers[index_numbers], list_divider[index_divider])
                pass
            else: #hier wird die check_list ausgefüllt
                check_list = is_number_prime(odd_numbers, list_divider, index_numbers, index_divider, check_list)
                #print(check_list)
            if index_divider == len(list_divider) - 1:  # hier ist der fehler;
                #print(check_list)
                is_False_in_list(check_list, prime_numbers, odd_numbers, index_numbers)
    print_all_prime_numbers(prime_numbers)

def is_number_prime(odd_numbers, list_divider, index_numbers, index_divider, check_list):
    #print(f"This ist the number: {odd_numbers[index_numbers]} and this is the divider {list_divider[index_divider]}")
    if odd_numbers[index_numbers] % list_divider[index_divider] == 0:
        check_list.append(False)
    else:
        check_list.append(True)
    return check_list

def is_False_in_list(check_list, prime_numbers, odd_numbers, index_numbers):
    if False in check_list:
        return None
    else:
        prime_numbers.append(odd_numbers[index_numbers])

def print_all_prime_numbers(prime_numbers):
    for number in prime_numbers:
        print(f"the number {number} is prime")

def is_two_in_range(range_list, prime_numbers):
    for number in range(range_list[0], range_list[1]):
        if number == 2:
            prime_numbers.append(2)
            return prime_numbers

def is_one_in_list(number_list):
    for number in number_list:
        if number == 1:
            number_list.remove(1)
            break

def main():
    make_parameters(get_range())

if __name__ == "__main__":
    main()