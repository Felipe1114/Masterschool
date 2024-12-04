def main():
  probability_for_succes = 2/6
  x = 3 #(x_num_of_succeses) (5) von num_of_dice sind erfolge
  n = 6 #(n_num_of_dice) kann sich ändern
  p = 1/3 #p_probability_for_succes

  # Probabilty_of_x_succeses
  P = binominal_distribution(n, p, x)

  print(P)



def binominal_distribution(n, p, x):
  """The formular for the binomal_distribution is: n/x * p**x * (1-p)**(n-x)"""
  Probability_of_x = (n / x *
                      p ** x *
                      (1 - p) ** (n - x))

  return Probability_of_x


if __name__ == "__main__":
  main()