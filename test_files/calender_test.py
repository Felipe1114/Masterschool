import calendar
from xmlrpc.client import DateTime

import tabulate


def make_calender(month, year):
  kalender = calendar.month(year, month)
  return kalender


aufgaben = [
  {'Name': 'Hackaton vorbereiten',
   'Beschreibung': 'Ideen sammeln',
   'Priorität': 4,
   'Datum': datetime("JJJ, MM, DD")
   },
  {"Name": "Meeting vorbereiten",
   "Beschreibung": "Notizen und Präsentation erstellen",
   "Priorität": 3,
   "Datum": datetime("JJJ, MM, DD")},
]






