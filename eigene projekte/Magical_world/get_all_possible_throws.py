from programm_modules import data_CRUM as dc
from programm_modules import probabilty_methods_multy_dice as pm
from programm_modules import make_csv_list as mcl


def main():
    all_possible_throws = mcl.get_all_possible_throws()
    all_possible_throws.insert(0, ["Würfelart", "bonus", "erschwernis"])

    for list in all_possible_throws:
        text = f"{str(list[0])}, {str(list[1])}, {str(list[2])}\n"
        dc.add_data(text, "all_possible_throws.csv")




if __name__ == "__main__":
    main()
