def go_thrue_list():
    list_from_1to4 = [1, 2, 3, 4]
    for index in range(len(list_from_1to4)):
        comprehend_list_numbers(index, list_from_1to4)

def comprehend_list_numbers(index, list_from_1to4):
    number_1 = list_from_1to4[index]
    for number_2 in list_from_1to4:
        if number_1 != number_2: print(number_1, number_2, sep=", ")

def main():
    go_thrue_list()

if __name__ == "__main__":
    main()