"""
warscheinlichkeit für einen erfolg ist:
  anzahl der erfolgsseiten / gesamt würfel seiten

regel:
    S = schwelle =  4(default)
    N = würfel seiten zahl (bei d6 = 6)
    E = warscheinlichkeit für erfolg (n/N)
        wenn die würfel augenzahl S oder höher zeigt


    P = warscheinlichkeit für einen misserfolg
    1 - E

    n = Seiten die erfolge(E) sind
        seiten >= S(4) (len([4, 5, 6])) = 3


    bsp.:
        d6:
            n = Seiten die erfolge sind
            seiten >= S(4) (len([4, 5, 6])) = 3

            N = gesamt zahl des wüfels (6)

            warscheinlichkeit(E) = n/N = 3/6

        d8:
            n = Seiten die erfolge sind
              seiten >= S(4) (len([4, 5, 6, 7, 8]) = 5

            N = gesamt zahl des würfels (8)

            warscheinlichkeit(E) = N/n = 5/8

    Erschwernisse:
        bei einer erschwernis(z) wird die schwelle(S) um z erhöht.

        bsp:
            erschwernis um 1:
            erschwernis(z) = 1
            neue schwelle = S(4) + z(1) = 5

    formel dafür:

    bsp:
        d8:
            n = Seiten die erfolge sind
              seiten > S(4) = (len([4, 5, 6, 7, 8])) = 5

            N = gesamte Seiten des würfels (8)
            z = erschwernis(z) (hier 1)

            warscheinlichkeit(E) = len(n[y:])/N

    Erleicheterungen:
    bei einer erleichterung wird ein zusätzlicher würfel(W) hinzugefügt.
    der key ist das Kürzel für den Würfel (d4, d6, usw...), der value ist e(die warcheinlichkeit für einen erfolg)

    E = das dictionary der würfel warscheinlichkeiten
    W = der zusatzwürfel-key
    E(W) = der ausgewählte zusatzwürfel aus dem dictionary

    zusatzwürfel:
        E(W) = {
        "d4": 1/4
        "d6": 3/6
        "d8": 5/8
        "d10": 7/10
        "d12": 9/12
        "d20": 17/20
        }

    die warscheinlichkeit für einen erfolg steigt durch einen zusatzwürfel.
    die formel für die erhöhte warscheinlichkeit ist:

        P1 = warscheinlichekit für misserfolg des ersten würfels
        P2 = warscheinlichekit für misserfolg des zweiten würfels

        n1 = warscheinlichkeit für erfolg  von worfel 1 = 1 - P1
        n2 = warscheinlichkeit für errofolg von würfel 2 = 1- P2

        formel:
            warscheinlichkeit für erfolg(n1&2) = 1 - (P1 x P2)

        beispiel:
            basis würfel (W1) = d8; E1 = 5/8
            zusatzwürfel (W2) = d6; E2 = 3/6

            P(W1) = 3/8
            P(W2) = 3/6

            n1&n2 = 1 - (3/8 * 3/6)

            n1&n2 = 1 - 0.0625
            n1&n2 = 0.9375

    """

def main():
    # only for testing
    pass


def get_prob_for_throw(N_from_dice:int=4, threshold_S:int=4, N_e_from_extra_dice:int=0, penalty_y:int=None) -> float:
    """calculates the probabilty of the chance of a success

    Args:
        N = all sides of a dice
        S = threshold to hit or overthrow
        E_base_dice = final probabilty
        y = penalty for probe

    Variables:
        n_1 = sides of dice higher then S

    Returns:

    """
    y = penalty_y
    N = N_from_dice
    N_e = N_e_from_extra_dice
    n_1 = get_n(N, threshold_S)

    E_base_dice = len(n_1[y:])/N # gibt bei einer erschwernis ab 1 einen fehler(index)

    if N_e is not None:
        n_2 = get_n(N_e, threshold_S)
        E_extra_dice = len(n_2[y:]) / N_e  # gibt bei einer erschwernis ab 1 einen fehler(index)

        # warscheinlichkeit mit bonus würfel ausrechen
        E_bonus = get_E_for_bonus()


        return

    return E_base_dice


def get_n(N_from_dice:int=4, threshold:int=4):
    n = []

    for i in range(N_from_dice):
        if i >= threshold:
            n.append(i)

    return n


def get_E_for_bonus():



if __name__ == "__main__":
    main()