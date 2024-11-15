# duplicate .jpg

with open("baseball.jpg", "bw") as pic:
    data = pic.read()

with open("baseball-copy.jpg", "bw") as pic:
    pic.write(data)