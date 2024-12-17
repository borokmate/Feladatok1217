'''
Töltsön fel egy listát 100db véletlen egész számmal -100 .. +100 tartományból!
a) Ezt követően határozza meg, hogy 0-tól nagyobb vagy kisebb számból van-e több!
b) Keresse meg az első 50-től nagyobb számot és írja ki a sorszámát! (0-tól indulót) Ha nincs ilyen, akkor pedig azt!
c) Van-e olyan eset, hogy két egymást követő szám közötti különbség meghaladja a 120-at?
'''

import random

rand_nums = [random.randint(-100, 100) for i in range(10)]

less_than_0 = 0
more_than_0 = 0
funf = -1
funf_finder = True
is_more_120 = False

for item in range(len(rand_nums)):

    if item < len(rand_nums)-1:

        if rand_nums[item] - rand_nums[item + 1] > 120:

            is_more_120 = True

    if funf_finder:

        if rand_nums[item] > 50:

            funf = item
            funf_finder = False

    if rand_nums[item] < 0:

        less_than_0 += 1
    
    elif rand_nums[item] > 0:

        more_than_0 += 1

print("Több pozitív, mint negatív" if more_than_0 > less_than_0 else "Több negatív, mint pozitív" if more_than_0 != less_than_0 else "Ugyanannyi van mindkettőből")
print(f"Első 50-nél többes index: {funf}" if funf >= 0 else "Nincs 50-nél nagyobb num")
print("120-as dolog van." if is_more_120 else "Nincs 120-as dolog")
print(rand_nums)