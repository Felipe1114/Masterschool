# eine for loop für die range
# herausfinden, ob die range 2>= ist --> 2 als festes print statement implementieren.
# herausfinden ob die zahl ungerade ist
# dann die zahl durch die hälfte aller vorheringen ungeraden zahlen teilen
    # warum nur die hälfte:
    # bsp: 0 - 100: 51 passt nicht mehr 2 mal in die hundert rein



def make_parameters(range_list):
    prime_numbers = []
    is_two_in_range(range_list, prime_numbers)
    odd_numbers = get_all_odd_numbers(range_list)
    middle_index = divide_len_odd_numbers(odd_numbers)
    list_for_dividing = split_odd_numbers(odd_numbers, middle_index)
    iterate_thrue_odd_numbers(odd_numbers, list_for_dividing, prime_numbers)

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

def iterate_thrue_odd_numbers(odd_numbers, list_for_dividing, prime_numbers):
    for index_numbers in range(len(odd_numbers)):
        for index_divider in range(len(list_for_dividing)):
            if odd_numbers[index_numbers] > list_for_dividing[index_divider] :
                is_number_prime(odd_numbers, list_for_dividing, index_numbers, index_divider, prime_numbers)
            else:
                break
    for number in prime_numbers:
        print(f"the number {number} is prime")

def is_number_prime(odd_numbers, list_for_dividing, index_numbers, index_divider, prime_numbers):
    if odd_numbers[index_numbers] % list_for_dividing[index_divider] == 0:
        return None
    elif index_divider == len(list_for_dividing) - 1:
        prime_numbers.append(odd_numbers[index_numbers])
    else:
        pass

def is_two_in_range(range_list, prime_numbers):
    for i in range_list:
        if i == 2:
            prime_numbers.append(2)


def main():
    make_parameters([1, 100]) # hier muss "get_range" rein. für den test ist hier was anderes

if __name__ == "__main__":
    main()