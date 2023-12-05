#!/usr/bin/env python3

if __name__ == '__main__':
    pass

#This program is designed to be the calculation system for Beckett Pizza Place BPP, to allow a quick and seamless calculation for the cost of customer orders.

#These are the variables for the pizza shop. They are the key facts that will be determined by user input.
Pizza_cost = 12
Pizza_number = 0
Tuesday = False
App_Used = False
Delivery_Required = False
Data_Valid = 0

#This is the information that is needed to be gathered from the user

#Checks the number of Pizzas Ordered
Pizza_number = input("Please enter the number of Pizzas ordered")

#Checking if the day is Tuesday
day = input("Enter the day of the week")
day = day.lower()
if day == "tuesday":
    Tuesday = True
else:
    Tuesday = False

#This checks if delivery is required
Delivery_Check = input("""Is delivery required (enter as yes / no)""")
Delivery_Check = Delivery_Check.lower()
if Delivery_Check == "yes":
    Delivery_Required = True
else:
    Delivery_Required = False

#This checks if the app was used
App_Check = input("""Was the app used (enter as yes / no)""")
App_Check = App_Check.lower()
if App_Check == "yes":
    App_Used = True
else:
    App_Used = False





