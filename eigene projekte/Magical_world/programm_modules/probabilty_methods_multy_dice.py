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

            E_bonus = 1 - (3/8 * 3/6)

            E_bonus = 1 - 0.0625
            E_bonus = 0.9375 # ergebnis ist falsch,... aber die formel ist richtig

    Erfolgsstärke (Strngt):
        Wenn ein würfel die maixmalzahl würfel (4 bei d4, 6 bei d6, usw...) dann explodiert der würfel.
        Je öfter ein würfel explodiert, desto besser ist das endergebnis.

        Die warscheinlichkeit dafür, dass ein würfel explodiert ist: 1/N
        Die warscheinlichkeit für 1, 2, 3 und 4 explosionen ist:

            1: 1-((N-1)/N ** 1)
            2: 1-((N-1)/N ** 2)
            3: 1-((N-1)/N ** 3)
            4: 1-((N-1)/N ** 4)


    """
def get_prob_for_throw(N_from_base_dice:int=4, N_e_from_extra_dice:int=None, penalty_y:int=0) -> tuple:
    """calculates the probabilty of the chance of a success

    Args:
        Nb = all sides of a dice
        S = threshold to hit or overthrow
        Eb = final probabilty
        y = penalty for probe

    Variables:
        n1 = sides of dice higher then S
        P1 = probability for fail (1-Eb)

        Ee = final probability of second dice
        P2 = probability for fail of socond dice (1-Ee)

        E_bonus = 1- ((1-Eb) * (1-Ee)) = 1- (P1 * P2)

    Returns:
        E_Base_dice(float): the probability for a success (with or without penalty)
        E_bonus(float): the probabilty for a success with bonus (with or without penalty)
    """
    threshold_S = 4 + penalty_y
    Nb = N_from_base_dice
    n1 = get_n(Nb, threshold_S)

    Eb = get_E(n1, Nb)

    strnght_list = get_throw_strnght(Nb)
    if N_e_from_extra_dice is not None:
        Ne = N_e_from_extra_dice
        n2 = get_n(Ne, threshold_S)

        Ee = get_E(n2, Ne)
        P1 = 1 - Eb
        P2 = 1 - Ee

        E_bonus = 1 - (P1 * P2)
        return E_bonus, strnght_list

    return Eb, strnght_list


def get_n(N_from_dice:int=4, threshold:int=4) -> list:
    """Gets all numbers >= threshold"""
    n = []

    for i in range(N_from_dice):
        if i+1 >= threshold:
            n.append(i+1)

    return n


def get_E(n:list, N:int) -> float:
    """E is the probabilty for a succes of a probe. the formular is: len(n)/N;

    Args:
        n: all possible numbers >= 4(S) of N
        N: sides of the dice (4, 6, 8, 10, 12 or 20)

    Returns:
        E(folat): the probabilty for an sucess
    """
    E = len(n) / N
    return E


def get_throw_strnght(N):
    """Strnght is the probability of rolling the highest number on a die and the probability that it repeats.
    formular:
    1 - ((N - 1) / N ** repeats)

    """
    strnght_list = []
    for i in range(4):
        strnght_list.append(1 - ((N - 1) / N ** (i+1)))

    return strnght_list