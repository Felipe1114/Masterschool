GRIESS = "Grieß"
MILCH = "Milch"
ZURUECK = "Zurück"

def input_abfrage():# fragt den aller ersten input ab -> personen oder mengenrechner
    personen_oder_umrechnen = input("Personenanzahl oder umrechnen? ")
    return personen_oder_umrechnen

def wie_viel_fuer_personen():# Funktion fuer Griess und Milchmenge abhaengig der Personen
    anzahl_personen = input("Fuer wie viele Personen kochst du? ")
    milch_menge = int(anzahl_personen) * 250
    menge_griess = int(anzahl_personen) * 37.5
    print(f"{milch_menge} ml Milch und {menge_griess} g Griess, ergeben {anzahl_personen} Portionen")

def griess_und_milch(Griess_oder_Milch):# Funktion fuer die Umrechnng von Griess und Milch zueinander
    if Griess_oder_Milch == GRIESS:#fragt ab, ob man die Grieß menge kennt
        menge_milch = input("Wie viel Milch hast du(nur die menge)? ")
        menge_griess = milch_zu_griess(menge_milch)
        print(f"Bei {menge_milch}ml Milch braubhst du {menge_griess}g Grieß, guten Apetit.")
    elif Griess_oder_Milch == MILCH:# fragt ab, ob man die Milch menge kennt
        menge_griess = input("Wie viel Griess hast du(nur die menge)? ")
        menge_milch = griess_zu_milch(menge_griess)
        print(f"Bei {menge_griess}g Grieß braubhst du {menge_milch}ml Milch, guten Apetit.")
    elif Griess_oder_Milch == ZURUECK:

    else:# gibt den loop zurück zur abfrage nach Grieß oder Milch
        print("falscher input, bitte versuche es nochmal")
        griess_und_milch(input("Brauchst du die Milch- oder Griessmenge? Bitte nur 'Milch' oder 'Grieß' eingeben "))

def griess_zu_milch(menge_griess): # rechnet aus, wie viel ml milch ich brauche wenn ich Xg Griess habe
    menge_milch = int(int(menge_griess) * 6.6)
    return menge_milch

def milch_zu_griess(menge_milch):# rechnet aus, wie viel g Griess ich braiche, wenn ich x g Griess habe
    menge_griess = int(menge_milch) // 6.6
    return menge_griess
#--------------------------------------
'''Diese Fukntion ist das hauptprogramm'''
def grieß_koch_helfer():# die main funktion, in der alle anderen funktionen enthalten sind.
    input_abfrage():
'''Diese Funktion ist das hauptprogramm'''
#--------------------------------------
# Ab hier fängt der eigentlich Code an

'''Dieser Abschnitt ist '''
grieß_koch_helfer()

if personen_oder_umrechnen == "Personen":
    wie_viel_fuer_personen()
elif personen_oder_umrechnen == "umrechnen":
    Griess_oder_Milch = input("Brauchst du die Milch- oder Griessmenge? ")
    griess_und_milch(Griess_oder_Milch)
else:
    print("falscher input")




