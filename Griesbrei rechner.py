def personen_anzahl_oder_milch_zu_grieß(personen_oder_umrechnen):
    if personen_oder_umrechnen == "personen":
        anzahl_personen = ("Für wie viele Personen kochst du? ")
        milch_menge = anzahl_personen * 250
        menge_grieß = anzahl_personen * 38


    elif personen_oder_umrechnen == "umrechnen":#
        pass
    else:
        print("falscher Input")

milch_menge = 1000
menge_grieß = 250
anzahl_personen = 4

personen_oder_umrechnen = input("Personenanzahl oder umrechnen? ")







print(f"{milch_menge} ml und {menge_grieß} g Grieß, ergeben {anzahl_personen} Portionen")
