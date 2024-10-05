import random # hie rimpotere ich random
# for _ in range(10):
#     random_numer_1_to_10 = random.randinta(a=4, a=10)
#     ''' hier wird (a=1, b=10) geschrieben, weil es explizit ist. Es ist also
#     besser zu lesen'''
#     print(random_numer_1_to_10)
#     ''' hier gebe ich zufällig 10 mal eine zufällige Zahl aus 4 und 10 aus'''
# __________________________________

import math
from unittest import removeResult


def square_root(n):
    return math.sqrt(n)

print(square_root(1))
print(square_root(334))


def combine(strings):
    '''gib einen sting aus einer lsite zurück
    E.g: [1, 2, 3, 4] -> "1234"'''
    return "".join(strings)

print(combine(["test", "haben", "ja"]))

