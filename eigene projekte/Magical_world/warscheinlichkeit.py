
"""

P(x \text{ Erfolge}) = n/x * p**x - (1-p)**{n-x}


Dabei gilt:
	•	n = Anzahl der Würfel (hier 6),
	•	x = Anzahl der Erfolge (hier 5, 4, 3, 2, 1 oder 0),
	•	p = Wahrscheinlichkeit für einen Erfolg (\frac{1}{3}),
	•	\binom{n}{x} = Binomialkoeffizient, der die Anzahl der Möglichkeiten darstellt, wie man x Erfolge aus n Versuchen auswählen kann. Der Binomialkoeffizient wird berechnet als:


\binom{n}{x} = \frac{n!}{x!(n-x)!}

"""

def warscheinlichkeit_fuer_erfolg(gewuensche_anzahl_erfolge, anzahl_wurfel, warscheinlichkeit_fuer_erfolge):
  n = anzahl_wurfel
  x = gewuensche_anzahl_erfolge
  p = warscheinlichkeit_fuer_erfolge
  if x>0:
    ergebnis = n/x * p**x - (1-p)**(n-x)
  else:
    ergebnis = 0
  return ergebnis


def main():
  gewuensche_anzahl_erfolge = 2 # wie viel erfolge erzielt werden sollen(max würfel anzahl)
  wuerfel_anzahl = 6 # wert kann sich verändern
  warscheinlichkeit_fuer_erfolg_pro_wuerfel = 6/gewuensche_anzahl_erfolge

  for wuerfel in range(wuerfel_anzahl):
    print(wuerfel)
    for erfolge in range(wuerfel):
      ergebnis = warscheinlichkeit_fuer_erfolg(erfolge, wuerfel_anzahl, warscheinlichkeit_fuer_erfolg_pro_wuerfel)
      print(f"Bei {wuerfel} Wuerfel(n) ist die warscheinlichkeit für {erfolge}Erfolge {ergebnis} prozent")



if __name__ == "__main__":
  main()