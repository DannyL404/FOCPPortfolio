#!/usr/bin/env python3

if __name__ == '__main__':

#A times table program focusing on the 7 times table

#The program is asking the user to imput a number
startnumber = input("Please enter a number between 0 and 12")
startnumber = int(startnumber)

#The program is calculating that number up to 12 x 7
while (0 <= startnumber <= 12):
    print(startnumber , "x 7 =" , startnumber * 7)
    startnumber += 1
#If the number entered is negative, the program will function in the same way but show largest number to smallest number
if (-12 <= startnumber <= 0):
    while (-12 <= startnumber <= 0):
        inputnumber = startnumber * -1
        print(inputnumber, "x 7 =", inputnumber * 7)
        startnumber += 1

