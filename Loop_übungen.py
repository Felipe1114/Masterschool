# print possible pairs:

'''def go_thrue_list():
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
    main()'''

# number pyramid:
def make_num_pyramid():
    for i in range(5):
        for j in range(i+1):
            print(i+1, end = "")
        print()

def main():
    make_num_pyramid()

if __name__ == "__main__":
    main()

# star pyramid reversed

'''def print_star_pyramid():
    for i in reversed(range(5)):
        for j in range(i+1):
            print("*", end = "")
        print()

def main():
    print_star_pyramid()

if __name__ == "__main__":
    main()'''

# star pyramid with input
'''def print_star_pyramid(height):
    for i in range(height):
        for j in range(i+1):
            print("*", end = "")
        print()

def main():
    height = int(input("how tall is the pyramid? "))
    print_star_pyramid(height)

if __name__ == "__main__":
    main()'''

# 5*3 star grid
'''def print_grid(row = 5, col = 3):
    for i in range(row):
        for j in range(col):
            print("*", end = "")
        print()

def main():
    print_grid()

if __name__ == "__main__":
    main()'''

# all persons eat the all food
'''def go_thrue_lists():
    persons = ["John", "Mary", "Yan", "Lu"]
    foods = ["Pizza", "Sushi", "Pasta", "Hummus"]
    for index_persons in range(len(persons)):
        for index_foods in range(len(foods)):
            print(f"{persons[index_persons]} eats {foods[index_foods]}")

def main():
    go_thrue_lists()
if __name__ == "__main__":
    main()'''

# number pyramid reversed:
'''def make_num_pyramid():
    for i in (range(5)):
        for j in range(i+1):
            print(j+1, end = "")
        print()

def main():
    make_num_pyramid()

if __name__ == "__main__":
    main()'''
'''
# ten first mulitplys:
def go_thrue_one_to_five():
    for i in range(5):
        multiply_i_ten_times(i)

def multiply_i_ten_times(i):
    print(f"First 10 Multiples of {i+1}:", end=" ")
    for j in range(10):
        print((i+1) * (j+1),"\t", end="")
    print()

def main():
    go_thrue_one_to_five()

if __name__ == "__main__":
    main()

for i in range(5):
    multiply_i_ten_times(i)
    print(f"First 10 Multiples of {i + 1}:", end=" ")
    for j in range(10):
        print((i + 1) * (j + 1), "\t", end="")
    print()
'''