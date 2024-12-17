"""
Állítsunk elő harmincelemű, nulla és kilenc közötti véletlen számokat tartalmazó listát! A számok egy útvonal magassági adatait jelentik. 
Meredek az útszakasz, ha legalább kettővel magasabb az aktuális hely, mint az előző. Hány meredek szakasz van az úton? És visszafelé?
"""

import random

nums = [random.randint(0, 9) for i in range(30)]

meredek = 0
vissza_meredek = 0

for item in range(len(nums)-1):

    if nums[item] <= nums[item+1] - 2:

        meredek += 1

    elif nums[item] - 2 >= nums[item+1]:

        vissza_meredek += 1

print(f"Jobbra meredek: {meredek} \nBalra meredek: {vissza_meredek}")
print("Itt a lista: ", nums)