
"""#öffnet ein file
fileobj = open("students.csv", "r")
data_base = fileobj.read()
print(len(data_base)) # -> 76; fileobj ist nun leer

data = fileobj.read(1)
print(len(data)) # -> 0

data = fileobj.read()
print(len(data)) # -> 0
# schließt das file. Jetzt kann nichts mehr mit dem file geamcht werden
fileobj.close()"""



# testen was passiert, wenn ein file geöffnet wird. in einer variablen gespeichert, und dann die variable gentutz wird
fileobj = open("students.csv", "r")
data = fileobj.read()
#fileobj.close()

print(data)
print("--")
print(data)