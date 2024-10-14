def verarbeite_schuelerdaten(schuelerliste):
    print("Schülerauswertung:")
    gesamtalter = 0
    for schueler in schuelerliste:
        gesamtalter += schueler['alter']
    durchschnittsalter = gesamtalter / len(schuelerliste)
    print(len(schuelerliste))
    print(schueler)
    print(f"Durchschnittsalter: {durchschnittsalter:.2f}")
    hoechster_notendurchschnitt = 0
    bester_schueler = None
    for schueler in schuelerliste:
        if schueler['notendurchschnitt'] > hoechster_notendurchschnitt:
            hoechster_notendurchschnitt = schueler['notendurchschnitt']
            bester_schueler = schueler['name']
    print(f"Bester Schüler: {bester_schueler} (Notendurchschnitt: {hoechster_notendurchschnitt})")
    hauptfach_anzahl = {}
    for schueler in schuelerliste:
        hauptfach = schueler['hauptfach']
        if hauptfach in hauptfach_anzahl:
            hauptfach_anzahl[hauptfach] += 1
        else:
            hauptfach_anzahl[hauptfach] = 1
    print("Schüler nach Hauptfach:")
    for hauptfach, anzahl in hauptfach_anzahl.items():
        print(f"{hauptfach}: {anzahl}")
    bericht = f"Gesamtanzahl Schüler: {len(schuelerliste)}\n"
    bericht += f"Durchschnittsalter: {durchschnittsalter:.2f}\n"
    bericht += f"Bester Schüler: {bester_schueler}\n"
    bericht += "Verteilung nach Hauptfach:\n"
    for hauptfach, anzahl in hauptfach_anzahl.items():
        bericht += f"  {hauptfach}: {anzahl}\n"
    return bericht


schueler = [
    {"name": "Emma Schmidt", "alter": 20, "notendurchschnitt": 1.3, "hauptfach": "Informatik"},
    {"name": "Lukas Weber", "alter": 22, "notendurchschnitt": 2.0, "hauptfach": "Ingenieurwesen"},
    {"name": "Sophie Müller", "alter": 19, "notendurchschnitt": 1.2, "hauptfach": "Biologie"},
    {"name": "Max Becker", "alter": 21, "notendurchschnitt": 2.3, "hauptfach": "Betriebswirtschaft"},
    {"name": "Anna Klein", "alter": 20, "notendurchschnitt": 1.7, "hauptfach": "Psychologie"},
    {"name": "Tim Hoffmann", "alter": 23, "notendurchschnitt": 2.1, "hauptfach": "Ingenieurwesen"},
    {"name": "Laura Wagner", "alter": 18, "notendurchschnitt": 1.0, "hauptfach": "Mathematik"},
    {"name": "Felix Schulz", "alter": 22, "notendurchschnitt": 1.8, "hauptfach": "Informatik"},
    {"name": "Julia Fischer", "alter": 21, "notendurchschnitt": 2.2, "hauptfach": "Betriebswirtschaft"},
    {"name": "Nico Schneider", "alter": 19, "notendurchschnitt": 1.3, "hauptfach": "Biologie"}
]

verarbeite_schuelerdaten(schueler)