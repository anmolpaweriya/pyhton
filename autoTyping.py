import pyautogui as pag
import time,random


print("------------ [ Anisole Creation ] -------------------")
print("\n\nchoose one operation ----------->")
print("\n\t 1.) txt File")
print("\t 2.) Enter strings")
choice = int(input("\n\nEnter your choice :-) "))

txtList = []

if(choice == 1):        # taking text from file
    file = open(input("\n\nEnter file name :-) ") , 'r')

    while True:
        line = file.readline()

        if not line:break
        txtList.append(line)

elif(choice == 2):      # taking strings from user
    while True:
        tempString = input("Enter Text (leave empty to stop): -) ")
        if(tempString == ""):break
        txtList.append(tempString)
    
repetations = int(input("Enter number of repitations : -) "))
gap = float(input("Enter gap Between repetations (sec) :-) "))

prefix = input("\nPrefix (Leave empty if you don't want)  :-) ")

for i in range(6):  # wait for 5 sec
    
    print(f"Wait for {6-i} sec ...",end = "\r")
    time.sleep(1)     
print()
for i in range(repetations):
    pag.write(prefix + random.choice(txtList))       # randomly choose string from list txtList
    pag.press('enter')                      # press Enter after typing string
    time.sleep(gap+0.01)
    print(f"repitation {i+1}")