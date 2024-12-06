from programm_modules import data_CRUM as dc
from programm_modules import probabilty_methods_d6 as pm


def main():
  file_name =  "probabilities.csv"

  num_of_dice = 6 #(n_num_of_dice) kann sich ändern
  probabiltay_for_success = round(2/6, 2) # 5 & 6 von [1, 2, 3, 4, 5, 6]

  result_list = pm.make_data_structure(num_of_dice, probabiltay_for_success)
  print(result_list)

  dc.save_data(result_list, file_name)

  better_probabiltay_for_success = round(3/6, 2) # 4 & 5 & 6 von [1, 2, 3, 4, 5, 6]
  new_result_list = pm.make_data_structure(num_of_dice, better_probabiltay_for_success)

  dc.add_data(new_result_list, file_name)

if __name__ == "__main__":
  main()