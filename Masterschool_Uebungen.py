#Übungen zu Listen
liste1 = [1, 2, 3, 4, 5]
liste1.remove(1)
print(liste1)
liste1.append(43)
liste1.insert(1, 33)
liste1.insert(3, "test")
print(liste1)

#ich kann elemente aus einer lsite herausholen, in dem ich diesen trick anwende
print(liste1[:1]+liste1[2:3]+liste1[5:6])
#hier durch werden nur bestimmte objekte aus der lsite herausgeholt,
#ohne dass die lsite zu einem String wird.

