def wie_viel_für_personen():
    anzahl_personen = input("Für wie viele Personen kochst du? ")
    milch_menge = int(anzahl_personen) * 250
    menge_grieß = int(anzahl_personen) * 37.5
    print(f"{milch_menge} ml Milch und {menge_grieß} g Grieß, ergeben {anzahl_personen} Portionen")

milch_menge = 1000
menge_grieß = 150
anzahl_personen = 4
personen_oder_umrechnen = input("Personenanzahl oder umrechnen? ")

if personen_oder_umrechnen == "Personen":
    wie_viel_für_personen()
elif personen_oder_umrechnen == "umrechnen":
    pass




