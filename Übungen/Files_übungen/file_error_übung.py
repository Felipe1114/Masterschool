
while True:
    try:
        filename = input("Please enter a filename: ")
        valid_files = ["grades.csv"]
        if filename in valid_files:
            with open(filename, "r") as fileobj:
                print("Length of file is: ", len(fileobj.read()))
                break
        else:
            raise Exception("File does not exist")
    except Exception as e:
        print(e)

program_survived = True
