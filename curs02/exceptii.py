variabila = input("Adauga un nr: ")
lista = [1, 2, 3]
try:
    if variabila.isdigit():
        raise ValueError6
    print(lista[3])
    variabila = int(variabila)
except ValueError:
    print("exceptie")
    if variabila.isdigit():
        variabila = int(variabila)
    a = None
except NameError:
    print("variabila nedefinita")
    a = None
except IndexError:
    print("Eroare de Index")
    print (lista[3:4])
except Exception:
    print("exceptie")
else:
    print("Nu exista exceptii")
finally:
    print("se ruleaza oricum")