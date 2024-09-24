'''Feste und nicht veränderbare Variablen'''

GRIESS = "Grieß"
MILCH = "Milch"
ZURUECK = "Zurück"

'''------------------------------------------------------------------------------------------------------------------'''

#Fragt ab, was man will: Menge für Personenzahl, oder Gries oder Milch Menge herausfinden'''

def input_abfrage():# fragt den aller ersten input ab -> personen oder mengenrechner
    personen_oder_umrechnen = input("Personenanzahl oder umrechnen? ")
    if personen_oder_umrechnen == "Personen":
        wie_viel_fuer_personen()
    elif personen_oder_umrechnen == "umrechnen":
        Griess_oder_Milch = input("Brauchst du die Milch- oder Griessmenge? ")
        griess_und_milch(Griess_oder_Milch)
    else:
        print("falscher input")

'''------------------------------------------------------------------------------------------------------------------'''
#Abhängig der Personen wird die Menge an Milch und Grieß zurück gegeben.
#Wie kann ich eine If funktion machen, die abhängig vom Typen funktioniert?

def wie_viel_fuer_personen():# Funktion fuer Griess und Milchmenge abhaengig der Personen
    anzahl_personen = input("Fuer wie viele Personen kochst du? ")
    is_int = 1
    anzahl_personen_int = int(anzahl_personen)
    if anzahl_personen_int.isdigit() == is_int.isdigit():
        milch_menge = int(anzahl_personen) * 250
        menge_griess = int(anzahl_personen) * 37.5
        print(f"{milch_menge} ml Milch und {menge_griess} g Griess, ergeben {anzahl_personen} Portionen")
    elif anzahl_personen == ZURUECK:
        input_abfrage()
    else:# wenn der input weder bei "if" noch bei "elif" passt, dann wird noch mal der input abgefragt
        print("falscher input")
        wie_viel_fuer_personen()

'''------------------------------------------------------------------------------------------------------------------'''
#Fragt ab, obich Milch habe und die Menge an Grieß dafür haben möchte, oder eben anders herum.

def griess_und_milch(Griess_oder_Milch):# Funktion fuer die Umrechnng von Griess und Milch zueinander
    if Griess_oder_Milch == GRIESS:#fragt ab, ob man die Grieß menge kennt
        menge_milch = input("Wie viel Milch hast du(nur die menge)? ")
        menge_griess = milch_zu_griess(menge_milch)
        print(f"Bei {menge_milch}ml Milch braubhst du {menge_griess}g Grieß, guten Apetit.")
    elif Griess_oder_Milch == MILCH:# fragt ab, ob man die Milch menge kennt
        menge_griess = input("Wie viel Griess hast du(nur die menge)? ")
        menge_milch = griess_zu_milch(menge_griess)
        print(f"Bei {menge_griess}g Grieß braubhst du {menge_milch}ml Milch, guten Apetit.")
    elif Griess_oder_Milch == ZURUECK:# geht wieder zurück in die algemeine Abfrage
        input_abfrage()
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
    input_abfrage()
'''Diese Funktion ist das hauptprogramm'''
#--------------------------------------
# Ab hier fängt der eigentlich Code an

grieß_koch_helfer()





