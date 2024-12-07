from programm_modules import data_CRUM as dc
from programm_modules import probabilty_methods_multy_dice as pm
from programm_modules import get_all_throws as mcl

def main():
    """Adds all possible throws and its probabilities to a csv file
    csv strukture:
    Würfelart, bonus, erschwernis, warscheinlichkeit für:, einfacher_erfolg, guter_erfolg, schwieriger_erfolg, extremer_erfolg
    """
    #get_probabilty_for_all_throws()
    data = dc.get_data("probabilty_all_throws.csv")

    list = rearange_data(data)

    list = change_data_types(list)

    best_throw_info = get_best_throw(list)
    print(best_throw_info)


def change_data_types(list):
    """changes all datatypes in list form string to int oder None"""
    for line in list:
        for i in range(len(line)):
            if line[i] == "None":
                continue
            else:
                check_num_type(line, i)

    return list


def check_num_type(line, i):
    if "." in line[i]:
        line[i] = float(line[i])
    else:
        line[i] = int(line[i])

    return line


def rearange_data(data):
    list = []
    # makes a line of lists out of data
    for item in data:
        list.append(item.split(","))
    # removes all unesecary items
    for line in list:
        for i in range(len(line)):

            if i + 1 == len(line):
                line[i] = line[i][1:-2]
            elif i == 0:
                continue
            else:
                line[i] = line[i][1:]

    #slices first element
    list = list[1:]

    return list


def get_probabilty_for_all_throws():
    """Calculates all propabilites for all possible throws

    success_1 - 4 : the propability for a repeat of the hightest num on a dice
    probability: dice is >= threshold(default=4)
    """
    all_throws = mcl.get_all_possible_throws()

    for throw in all_throws:

        dice, bonus, penalty = throw
        throw_result = pm.get_prob_for_throw(dice, bonus, penalty)
        probability = throw_result[0]
        success_1, success_2, success_3, success_4 = throw_result[1]

        text = f"{dice}, {bonus}, {penalty}, {probability}, {success_1}, {success_2}, {success_3}, {success_4}\n"
        dc.add_data(text, "probabilty_all_throws.csv")


def get_all_possible_throws():
    """gets the list of all possible throws, insterts the header for a csv file and saves the list in a csv file"""
    all_possible_throws = mcl.get_all_possible_throws()
    all_possible_throws.insert(0, ["Würfelart", "bonus", "erschwernis"])

    for list in all_possible_throws:

        text = f"{str(list[0])}, {str(list[1])}, {str(list[2])}\n"
        dc.add_data(text, "all_possible_throws.csv")


def get_best_throw(list):

    dice = 0
    best_prob = 0
    best_success_1 = 0
    best_success_2 = 0
    for line in list:


    # fehler: d4 hat die besten kritische treffer chanchen. daher wird immer d4
    # ausgegeben.
    # andere formel benötigt
        if (line[3] > best_prob and
                line[5] > best_success_1 and
                line[6] > best_success_2):
            dice = line[0]
            best_prob = line[3]
            best_success_1 = line[5]
            best_success_2 = line[3]

    return dice, best_prob, best_success_1, best_success_2




if __name__ == "__main__":
    main()