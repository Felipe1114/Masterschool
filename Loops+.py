

'''
katze_count = 0
for tierchen in pets:
    if tierchen == "Katze":
        katze_count = katze_count +1
    else:
        pass

print(f"Katze kommt in der Liste {katze_count} mal vor")
'''
pets = ["Katze", "Hamster", "Hund", "Fliege"]

for i in range(len(pets)):
    if pets[i] == "Hund":
        pets[i] = "Verkauft"


print(f"liste nachher{pets}")