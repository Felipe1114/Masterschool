from programm_modules import data_CRUM as dc
from programm_modules import probabilty_methods_multy_dice as pm

def main():
    E = pm.get_prob_for_throw(6, 8)
    print(E)

if __name__ == "__main__":
    main()
