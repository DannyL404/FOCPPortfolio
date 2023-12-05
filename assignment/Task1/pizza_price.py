#!/usr/bin/env python3

if __name__ == '__main__':
    pass

#This program is designed to be the calculation system for Beckett Pizza Place BPP, to allow a quick and seamless calculation for the cost of customer orders.

#These are the variables for the pizza shop. They are the key facts that will be determined by user input.
Pizza_cost = 12
Pizza_number = 0
Pizza_Type = []
Tuesday = False
App_Used = False
Data_Valid = 0

#This is the information that is needed to be gathered from the user

#Checking if the day is Tuesday
Tuesday = input("""Is today Tuesday? \n Please enter 'True' or 'False'""")
while Data_Valid == 0:
    if Tuesday == "True":
        Tuesday = bool(Tuesday)
        Data_Valid += 1
    elif Tuesday == "False":
        Tuesday = bool(Tuesday)
        Data_Valid += 1
    else:
        Tuesday = input("""Is today Tuesday? \n Please enter 'True' or 'False'""")

#Checking if the app was used.
App_Used = input("""Is today Tuesday? \n Please enter 'True' or 'False'""")
while Data_Valid == 0:
    if App_Used == "True":
        App_Used = bool(App_Used)
        Data_Valid += 1
    elif App_Used == "False":
        App_Used = bool(App_Used)
        Data_Valid += 1
    else:
        App_Used = input("""Is today Tuesday? \n Please enter 'True' or 'False'""")

print(type(Tuesday))