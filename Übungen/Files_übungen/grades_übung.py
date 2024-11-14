with open("grades.csv") as csvfile:
    lines = csvfile.readlines()
    grades = []
    for line in lines:
        line_content = line.split(",")
        if len(line_content[1]) < 3:
            grades.append(int(line_content[1]))
    avg = sum(grades) // len(grades)
    print(avg)
