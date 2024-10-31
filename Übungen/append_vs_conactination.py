# unterschied zwischen .append() und concatination

a_list = [1, 2, 3]
b_list = a_list
print("hier wurde eine liste geklont")
print("b_list enthält den gleichen inhalt wie a_list: ", a_list == b_list)
print("b_list ist a_list: ", a_list is b_list)

b_list.append(4)
print("jetzt wurde mit append, beide listen aktualisert")
print(b_list)
print(a_list)
print("b_list enthält den gleichen inhalt wie a_list: ", a_list == b_list)
print("b_list ist a_list: ", a_list is b_list)

b_list += [5]
print("jetzt wurde mit += die zahl 5 an die liste angehängt")
print(a_list)
print(b_list)
print("b_list enthält den gleichen inhalt wie a_list: ", a_list == b_list)
print("b_list ist a_list: ", a_list is b_list)

b_list = b_list + [6]
print("jetzt wurde mit concatination die zahl 7 an liste b_list angehängt")
print(a_list)
print(b_list)
print("b_list enthält den gleichen inhalt wie a_list: ", a_list == b_list)
print("b_list ist a_list: ", a_list is b_list)
