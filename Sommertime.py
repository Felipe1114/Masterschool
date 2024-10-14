def get_numbers():
    return int(input("Type in a number: "))

def sum_numbers():
    result = 0
    while result < 1000:
        result += get_numbers()
    print(result)

def main():
    sum_numbers()

if __name__ == "__main__":
    main()