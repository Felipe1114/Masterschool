from programm_modules import data_CRUM as dc
from programm_modules import probabilty_methods_multy_dice as pm
from programm_modules import get_all_throws as mcl

def main():
    """Adds all possible throws and its probabilities to a csv file
    csv strukture:
    Würfelart, bonus, erschwernis, warscheinlichkeit für:, einfacher_erfolg, guter_erfolg, schwieriger_erfolg, extremer_erfolg
    """
    get_probabilty_for_all_throws()


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
    all_possible_throws = at.get_all_possible_throws()
    all_possible_throws.insert(0, ["Würfelart", "bonus", "erschwernis"])

    for list in all_possible_throws:

        text = f"{str(list[0])}, {str(list[1])}, {str(list[2])}\n"
        dc.add_data(text, "all_possible_throws.csv")


if __name__ == "__main__":
    main()