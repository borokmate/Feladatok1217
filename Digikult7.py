"""
Kihívást jelentő feladat: Állítsunk elő nyolcvanelemű, −5 és 3 közötti egész számokból álló listát! 
A számok egy úszó palackorrú delfin magasságát jelentik. 
A delfin ki-kiugrál a vízből, ilyenkor pozitív a magassága. 
Nulla a magasság, amikor a felszínen úszik, negatív, amikor a víz alatt. Írjunk programot, ami választ ad a következő kérdésekre!

    a. Az út mekkora részét tette meg a delfin a vízben, illetve a víz alatt? A válaszok megadhatóak törtszámként és százalékként is.
    b. Víz alatt vagy víz felett volt-e többet a delfin? A vízfelszínen való utazás egyik esetbe sem számít bele.
    c. Milyen hosszú volt a leghosszabb kiugrása? Az út hányadik pontjánál kezdődött?
    d. Hányszor törte át a vízfelszínt, azaz hányszor követ a listában negatív számot pozitív, vagy fordítva?
    e. Mély merülésnek számít, ha a delfin −4-es vagy −5-ös mélységben van. Az út során hányszor merült mélyre? 
    Figyeljünk arra, hogy például a négy −2, −4, −5, −5, 3 útvonal csak egy mélyre merülést jelent!

"""

import random

nums = [random.randint(-5, 3) for i in range(80)]

vizben = 0

felett = 0
alatt = 0

most_lang = 0
start = 0
end = 0

attores = 0

mely_check = True
melyre = 0


for item in range(len(nums)):

    if item < len(nums) - 1:

        if nums[item] > 0:
            
            lang = 0
            j = 0

            while nums[item + j] > 0:

                lang += 1
                j += 1

                if len(nums) == item + j:
                    if lang > most_lang:
                        most_lang = lang
                        start = item
                        end = item + j - 1
                    break
            
            else:
                if lang > most_lang:
                    most_lang = lang
                    start = item
                    end = item + j - 1
        
        if nums[item] > 0 and nums[item + 1] < 0:

            attores += 1

        elif nums[item] < 0 and nums[item + 1] > 0:

            attores += 1

    if nums[item] <= -4:

        if mely_check:

            melyre += 1
            mely_check = False
    
    else:

        mely_check = True


    if nums[item] > 0:

        felett += 1
    
    elif nums[item] < 0:

        alatt += 1

    if nums[item] <= 0:

        vizben += 1

print("Vizben halad a delphin:", vizben/len(nums)*100, "százalékban")
print("Többt van fent, mint lent" if felett > alatt else "Többt van lent, mint fent" if felett != alatt else "Ugyanannyit tölt mindkét helyen")
print(f"Kezdete: {start} \nVége: {end}")
print(f"Áttörés: {attores}")
print(f"Mélyre ment: {melyre}")

