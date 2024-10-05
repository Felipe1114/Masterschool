def get_numbers_from_user():
    numbers = []
    n = int(input("How many numbers will you enter? "))
    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num) # erstellt die liste "numbers" aus den eingegebenen zahlen
        #print(numbers) # die liste wird einwandfrei erstellt
    return numbers


def filter_negative_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num >= 0:
            new_numbers.append(num)
    return new_numbers # return value war falsch eingrückt



def sum_numbers(numbers):
    return sum(numbers)


def main():
    user_numbers = get_numbers_from_user()
    print("user_numers ist: ", user_numbers)
    positive_numbers = filter_negative_numbers(user_numbers)
    print("prositive_numbers ist: ", positive_numbers)
    total_sum = sum_numbers(positive_numbers)

    print(f"Sum of non-negative numbers: {total_sum}")


if __name__ == "__main__":
    main()
#print(3+3+3+4)