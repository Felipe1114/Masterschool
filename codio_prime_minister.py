# eine for loop für die range
# herausfinden, ob die range 2>= ist --> 2 als festes print statement implementieren.
# herausfinden ob die zahl ungerade ist
# dann die zahl durch die hälfte aller vorheringen ungeraden zahlen teilen
    # warum nur die hälfte:
    # bsp: 0 - 100: 51 passt nicht mehr 2 mal in die hundert rein
def make_parameters(range_list):
    prime_numbers = []
    is_True = is_one_or_two_in_range(range_list)
    if is_True == True:
        return prime_numbers = [1, 2]
    odd_numbers = get_all_odd_numbers(range_list)
    middle_index = divide_len_odd_numbers(odd_numbers)
    list_for_dividing = split_odd_numbers(odd_numbers, middle_index)
    iterate_thrue_odd_numbers(list_for_dividing)

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

def iterate_thrue_odd_numbers(odd_numbers, list_for_dividing):
    for index_odd_numbers in range(len(odd_numbers)):
        for index_of_divider in range(len(list_for_dividing)):
            is_odd_greater = is_odd_number_greater_divider(odd_numbers[index_odd_numbers], list_for_dividing[index_of_divider])
            if is_odd_greater == True:
                if odd_numbers[index_odd_numbers] % list_for_dividing[index_of_divider] == 0:
                    pass
                else:
                    print()
    # hier komme ich grade nicht weietr
    # ich gehe hier alle zahelen druch und teile sie mit den möglichen ungeraten zahlen
    # ich muss noch die funktion einbauchen, mit der ich richtig teile
    # es ist wichtig, dass wirklich alle zaheln mit allen möglichen zaheln geteilt werdene


def is_one_or_two_in_range(range_list):
    return 1 in range_list or 2 in range_list

def is_divider_greater_odd_number(odd_number, divider):
    return odd_number > divider



def main():
    make_parameters(get_range())

if __name__ == "__main__":
    main()