
"""ef functie():
    global mesaj
    mesaj = "Buna seara"
    print(mesaj)
"""
msg = "Buna ziua"
def functie():
    def functie2():
        print(f"A doua functie: {msg}")
    msg = "Buna seara"
    functie2()
    print(f"functie: {msg}")
#functie()
#print(mesaj)

functie()