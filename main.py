#Created by KrazyKirby99999 on 9/5/2020

import os

dirs = {}


os.chdir(os.getcwd()+"\projects")

for i in os.listdir(os.getcwd()):
    if not "." in i:
        dirs[int(i.partition("_")[0])] = i

for i in range(1,15):
    print(dirs[i])

uInput = input("Enter number id of project to run(1-15): ")

os.chdir(dirs[int(uInput)])
os.system("cls")
input(dirs[int(uInput)] + "\nPress Enter to Continue")
os.system("cls")
os.system("python app.py")

