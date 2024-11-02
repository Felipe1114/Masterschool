'''# dictionary erstellen: dictionary zu den olympischen medailien der USA

medals = {}
medals["gold"] = 33
medals["silver"] = 17
medals["bronze"] = 12

print(medals)
'''
'''swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}
swimmers["Phelps"] += 5
del swimmers["Lochte"]
print(swimmers)'''
#erstelle eine liste der "keys" des dictionarys medal_events
'''medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events =[]
for event in medal_events.keys():
    events.append(event)

print(events)
'''
# füge die summe aller meailien in einer liste zusammen:
'''medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
total_medals = 0
for key in medal_events:
    total_medals += medal_events[key]

print(total_medals)'''
'''
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.items())
print(list(inventory.items()))
for item in inventory.items():
    print(f"Got {item[0]} that maps to {item[1]}")'''

# die summer der medailien aller frauen:
'''uk_medals = {
    'Shooting (Women)': 4,
    'Shooting (Men)': 4,
    'Fencing (Women)': 4,
    'Fencing (Men)': 2,
    'Judo (Women)': 6,
    'Judo (Men)': 2,
    'Swimming (Women)': 1,
    'Swimming (Men)': 3
}
total_medals = 0
for key, val in uk_medals.items():
    if key.endswith("(Women)"):
        total_medals += val

print(total_medals)'''
'''# Name: Gemma Newton
# Age: 17
# City: Brighton

student_info = {
    "Name": "Gemma Newton",
    "Age": 17,
    "City": "Brighton"
}

print(student_info)'''

'''
US_medals = {"Swimming": 13, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 6, "Archery": 5, "Cycling - Track": 1, "Equestrian": 2, "Golf": 17, "Weightlifting": 1}

for key, val in US_medals.items():
    if val > 5:
        print(key)'''

'''str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for letter in str1:
    if letter not in freq:
        freq[letter] = 0
    freq[letter] += 1

print(freq)'''

list_of_cars = ["Ford", "Toyota", "Hyundai", "Toyota", "Hyundai", "Ford", "Ford", "Toyota", "Toyota", "Toyota","Toyota", "Hyundai", "Toyota", "Hyundai", "Toyota", "Hyundai", "Ford", "Ford", "Ford"]
freq_brands = {}
for brand in list_of_cars:
    if brand not in freq_brands:
        freq_brands[brand] = 0
    freq_brands[brand] += 1

print(freq_brands)