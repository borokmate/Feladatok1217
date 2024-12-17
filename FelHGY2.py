"""
Adott egy
varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]
lista.
Készítsen programot, amely bekér egy városnevet és ha az szerepel a listában, 
akkor kiírja az azt követő város nevét! Ha a bekért város az utolsó város volt, akkor jelezze, 
hogy nincs következő! Amennyiben pedig nem szerepel a listában, akkor vegye fel a lista végére!
"""

varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

running = True

if input("Teszt? Y/N") == "y" or "Y":
    test = True
else:
    test = False

while running:

    varos = input("Give város bitte: ")

    if varos in varosok:

        if varosok.index(varos) == len(varosok)-1:

            print("Nincs következő város")

        else:

            print(varosok[varosok.index(varos)+1])
    
    else:

        varosok.append(varos)

    if test:
        print("uhhhh: ", varosok)