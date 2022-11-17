a = 3  # int
b = 3.4
c = 1j
print(type(c))
# b = int(b)
# print(b)
# c = a % b #module
# c = a // b #impartire exacta
# c = a ** b
# print(c)
# print(5 != 5 and 4>3)
# print(7 in not 7)
# print(1 in [1,2,3]
# print(1 not in [1,2,3])

# variabila = 5
# print(variabila == 4)
# a=1
# a = a+1
# a =+ 1 incrementare

# variabila = "Ana are '3\' mere"
# variabila = "Ana are '3' mere"
nr_mere = 3
nr_pere = 4
variabila = "Ana are " + str(nr_mere) + " mere"
variabila = "Ana are {1} mere si {0} pere".format(nr_mere, nr_pere)
variabila = f"Ana {nr_mere} mere si {nr_pere} mere"
print(variabila)

lista = [3, 4, 'string', [1, "2", 'element']]

print(lista[3][2][2])

tuplu = (1,)

print(type(tuplu))

dictionar = {"cheie": "valoare", "cheie1": "3"}
# print(dictionar["cheie"])
# print(dictionar.get('cheie2',5))
dictionar["cheie1"] = 6
dictionar.update({'cheie2': 5, 'cheie3': 5})
print(dictionar)
print(dictionar.keys())
print(dictionar.values())

seturi = {1, 3, '5'}
print(seturi)
print(list(seturi))

mesaj = "variabila 1 e mai mica";
# if
print(2 ** 32)
variabila1 = 1
variabila2 = 2
# if variabila1 == variabila2:
#    mesaj = "egalitate"
# elif variabila1 > variabila2:
#    mesaj = "variabila 1 este mai mare"
mesaj = "egalitate" if variabila1 == variabila2 else "variabila 1 e mai mica"
print(mesaj)

while variabila1 > variabila2:
    print(variabila2)

for i, v in enumerate("Ana are mere"):
    print(i, v)

dictionar = {"carte1": 1, "carte2": 2, "carte3": 3}
for i, v in dictionar.items():
    print(i, v)
for i in dictionar.items():
    index, value =i
    print(index, value)
