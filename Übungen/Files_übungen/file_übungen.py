with open("orig.txt", "r") as fileobj:
    datalines = fileobj.read()


with open("reverse.txt", "w") as fileobj:
    new_text = ""
    for i in range(len(datalines)-1, -1, -1):
        new_text = new_text + f"{datalines[i]}"
    new_text = new_text.replace(" ", "\n")
    fileobj.write(new_text)
