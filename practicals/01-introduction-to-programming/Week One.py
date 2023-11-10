#!/usr/bin/env python3

if __name__ == '__main__':
#Week One of my Python Portfolio

    print("Hello World!")
#This is the first step to becoming a programmer.

#The same program that is now displaying my name.
print("Hello, Dan!")

#A program that takes a temperature in Celsius and converts to Farenheit.
celsiustemp = input("Please enter the temperature in Celsius.")
celsiustemp = float(celsiustemp)
fahrenheittemp = (1.8 * celsiustemp) + 32
print("The tempartature was" , celsiustemp , "in Celcius and is" , fahrenheittemp , "in Farenheit.")

#This program creates the batting average for Geoffery Boycott.
#The completed innings are calculated by substracting the times not out by the amout of times batted.
completedinnings = 1014 - 162
#The batted average is calculated by dividing the number of runs with the completed innings
battedaverage = 48426 / completedinnings
print("The batted average for Geoffery Boycott is" , battedaverage)

#This program calculates the number of groups required in a computing lab
#program for 113 students
print(113 // 24 , 113 % 24)
print(175 // 24 , 175 % 24)
print(12 // 24 , 12 % 24)