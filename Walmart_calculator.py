'''Ich habe einen preis.
darauf wird noch eine stauer aufgerechnet.
der kunde zahlt mti einem wert.
das programm rechnet den preis mit der steur zusammen und gibt die differenz zu dem Zahlwert aus
'''
def change_back():
    price = article_price()
    #full_price = price + price * 0.115 <-- diese linefunktioniert
    full_pric = full_price(price) #<-- diese line funktioniert nicht
    return calculate_change(full_pric)

# in dieser Funktion ist das problem
def full_price(price):
    full_pric = price + price * 0.115
    return full_pric # hier ist das problem ?

def article_price():
    return float(input("How much does the article cost?(a float number, please) "))

def calculate_change(full_price):
    costumer_amount = float(input("How much money gives the costumer?(a float number, please) "))
    return costumer_amount - full_price

def main():
    print(f"the cosutmer gets {change_back()}$ back.")

if __name__ == "__main__":
    main()