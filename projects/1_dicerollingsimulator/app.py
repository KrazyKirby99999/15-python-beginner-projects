import random
import json
import os

with open("dice.json") as json_file: 
    dicePatterns = json.load(json_file)

run = 1

while run != 0:
    print(dicePatterns[str(random.randint(1,6))] + "\n\n" + dicePatterns[str(random.randint(1,6))])
    try:
        run = int(input("Enter 0 to exit\n"))
        os.system("cls")
    except:
        os.system("cls")
    

    