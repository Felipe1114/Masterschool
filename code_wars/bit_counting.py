def count_bits(n):
    """Schreibe eine Funktion, die eine Ganzzahl (Integer) als Eingabe erhält und die Anzahl der Bits zurückgibt, die in der Binärdarstellung dieser Zahl gleich 1 sind. Du kannst davon ausgehen, dass die Eingabe eine nicht-negative Zahl ist.
    mit bin(n) erhält man den binär-code für das Argument.
    Der output sieht so aus: 0bxxxx.
    0b muss weg, also nutzte ich slicing [2:]
    ich wandle dann das ergebnis in eine liste um und zähle alle einsen.
    """
    bit_num = list(bin(n)[2:]).count("1")
    return bit_num



