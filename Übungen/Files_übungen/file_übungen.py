with open("grades.csv", "r") as fileobj:
    data = fileobj.read()

with open("grades2.csv", "w") as fileobj:
    fileobj.write(data)
    for i in range(10):
        fileobj.write(f"das ist die{i+1}. Zeile, die hinzugefügt wurde")

