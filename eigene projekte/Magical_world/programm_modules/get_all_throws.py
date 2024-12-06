"""
Mögliche würfe:
1. alle 6 würfel und ihre warscheinlichkeiten
2. alle 6 würfel mit erschwernissen(1-5) und ihre warscheinlichkeiten
3. alle 6 würfel mit bonus (je alle 6 bonus würfel) und ihre warscheinlichkeiten
4. alle 6 würfel mit erschwernissen(1-5) und bonus (je alle 6 bonus würfel) und ihre warscheinlichkeiten

vier for schleifen. Jeder forschleifen behandelt einen der 4 punkte.

daten format:
liste_dices = [4, 6, 8, 10, 12, 20]
liste_erschwernisse =[1, 2, 3, 4, 5]
"""

LIST_DICES = [4, 6, 8, 10, 12, 20]
LIST_PENALTY =[1, 2, 3, 4, 5]

def get_all_possible_throws():
    """gets all possible throws in for lists"""
    list_1 = get_1()
    list_2 = get_2()
    list_3 = get_3()
    list_4 = get_4()

    all_throws = seam_lists(list_1, list_2, list_3, list_4)
    return all_throws



def get_1():
    """All throws with all dices"""
    list = []
    for dice in LIST_DICES:
        list.append([dice, None, 0])
    return list


def get_2():
    """All throws with All dices an penalties"""
    list = []
    for dice in LIST_DICES:
        for penalty in LIST_PENALTY:
            list.append([dice, None, penalty])
    return list


def get_3():
    """All Throws with all dices and all bonus dices"""
    list = []
    for dice in LIST_DICES:
        for bonus in LIST_DICES:
            list.append([dice, bonus, 0])
    return list


def get_4():
    """All Throws with all dices, penalties and bonus dices """
    list = []
    for dice in LIST_DICES:
        for penalty in LIST_PENALTY:
            for bonus in LIST_DICES:
                list.append([dice, bonus, penalty])
    return list


def seam_lists(list1, list2, list3, list4):
    """puts all lists together, to one large list"""
    all_lists = [list1, list2, list3, list4]
    new_list = []

    for list in all_lists:
        for item in list:
            new_list.append(item)

    return new_list








