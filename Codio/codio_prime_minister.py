def make_parameters(range_list):
    prime_numbers = []
    is_two_in_range(range_list, prime_numbers)
    odd_numbers = get_all_odd_numbers(range_list)
    middle_index = divide_len_odd_numbers(odd_numbers)

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
    return odd_numbers

    for index_numbers in range(len(odd_numbers)):
    else:
    for number in prime_numbers:
        print(f"the number {number} is prime")

def is_two_in_range(range_list, prime_numbers):
            prime_numbers.append(2)


def main():

if __name__ == "__main__":
    main()