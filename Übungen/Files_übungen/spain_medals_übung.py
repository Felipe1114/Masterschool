def is_woman_and_gold(list):
    event = list[2][:7]
    medal = list[3].strip()
    woman = "Women's"
    gold = "Gold"
    if woman == event and gold in medal:
        return True
    else:
        return False




with open("spain-medals.csv", "r") as csvfile:
    lines = csvfile.readlines()
    women_gold_winners = []
    for i in range(len(lines)):
        if i-1 > 0:
            list = lines[i-1].split(",")
            if is_woman_and_gold(list):
                women_gold_winners.append(list[0])
    print(women_gold_winners)

