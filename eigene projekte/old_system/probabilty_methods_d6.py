def binominal_distribution(num_of_dice, probabilty_for_succes, successes):
  """The formular for the binomal_distribution is: n/x * p**x * (1-p)**(n-x)
  Errechnet die warscheinlichkeit für x erfolge bei y würfel
  """
  if successes == 0: return 0

  Probability_of_x = (num_of_dice / successes *
                      probabilty_for_succes ** successes *
                      (1 - probabilty_for_succes) ** (num_of_dice - successes))

  return Probability_of_x


def make_data_structure(num_of_dice, probability_for_success):
  """Packt alle ergebnisse in eine CSV kompatible liste.
  Nimmt num_of_dice(die maximal zahl) und geht alle möglichen ergebnisse durch


  Var_description:
    x_num_of_dice und num_of_dice muss 1 höher sein, weil range sonst nicht bis max würfel geht

  Returns:
    probabilty_list(list): a list for an svg file
  """
  probability_list = ['chance auf erfolg, würfel, anzahl_gewünschter erfolge(x), prozent für x erfolge\n']
  for x_num_of_dice in range(num_of_dice+1):

    for scuccesses in range(x_num_of_dice+1):

      result = binominal_distribution(x_num_of_dice+1, probability_for_success, scuccesses)
      probability_list.append(f"{probability_for_success},{x_num_of_dice}, {scuccesses}, {round(result, 2)}\n")

  return probability_list

