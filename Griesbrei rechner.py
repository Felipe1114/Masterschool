GRIEß = "Grieß"
MILCH = "Milch"

def wie_viel_für_personen():# Funktion für Grieß und Milchmenge abhängig der Personen
    anzahl_personen = input("Für wie viele Personen kochst du? ")
    milch_menge = int(anzahl_personen) * 250
    menge_grieß = int(anzahl_personen) * 37.5
    print(f"{milch_menge} ml Milch und {menge_grieß} g Grieß, ergeben {anzahl_personen} Portionen")

def grieß_und_milch(Grieß_oder_Milch):# Funktion für die Umrechnng von Grieß und Milch zueinander
    if Grieß_oder_Milch == GRIEß:
        wie_viel_milch = input("Wie viel Milch hast du? ")


    elif Grieß_oder_Milch == MILCH:
        wie_viel_grieß = input("Wie viel Grieß hast du? ")
        grieß_zu_milch(wie_viel_grieß)

def grieß_zu_milch(wie_viel_grieß):
    pass

def milch_zu_grieß(wie_viel_milch):
    pass

milch_menge = 1000
menge_grieß = 150
anzahl_personen = 4
personen_oder_umrechnen = input("Personenanzahl oder umrechnen? ")

if personen_oder_umrechnen == "Personen":
    wie_viel_für_personen()
elif personen_oder_umrechnen == "umrechnen":
    Grieß_oder_Milch = input("Brauchst du die Milch- oder Grießmenge? ")
    grieß_und_milch(Grieß_oder_Milch)
else:
    print("falscher input")




