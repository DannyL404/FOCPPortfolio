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
Total_Cost = float(0)

#Creating a nicely formatted header for the program to be displayed to the user
print("BPP Pizza Price Calculator")
print("==========================")

#This is the information that is needed to be gathered from the user

#Checks the number of Pizzas Ordered
while True:
    try:
        Pizza_number = input("Please enter the number of Pizzas ordered")
        Pizza_number = int(Pizza_number)
        break
    except:
        print("invalid input, please enter a valid whole number value")


while True:
    day = input("Enter the day of the week")
    day = day.lower()
    if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        Tuesday = (day == "tuesday")
        break
    else:
        print("Invalid input, please enter a valid day of the week.")

if day == "tuesday":
    Tuesday = True

#This checks if delivery is required
while True:
    Delivery_Check = input("""Is delivery required (enter as yes / no)""")
    Delivery_Check = Delivery_Check.lower()
    if Delivery_Check in ["yes", "no"]:
        Delivery_Required = (Delivery_Check == "yes")
        break
    else:
        print("Invalid input, please enter, yes or no")

if Delivery_Required == "yes":
    Delivery_Required = True

#This checks if the app was used
while True:
    App_Check = input("""Was the app used (enter as yes / no)""")
    App_Check = App_Check.lower()
    if App_Check in ["yes", "no"]:
        App_Used = (App_Check == "yes")
        break
    else:
        print("Invalid input, please enter, yes or no")

if App_Used == "yes":
    App_Used = True

#This part of the program will calculate the output
Total_Cost = Pizza_cost * Pizza_number


if Tuesday == True:
    Total_Cost *= 0.5

if App_Used == True:
    Total_Cost *= 0.75

if Delivery_Required == True and Pizza_number <= 5:
    Total_Cost += 2.5
#Displays the total cost to the user
print(f"Total Price: £{Total_Cost:.2f}")
