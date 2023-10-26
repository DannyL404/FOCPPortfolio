#!/usr/bin/env python3

if __name__ == '__main__':

#Password Program v2 - this is designed to keep running until a valid password is selected
#Begins by setting every password as false and specifying the bad passwords the program can recognise.
passwordvalid = False
badpasswords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

#A loop to test all the conditions until the input passes all checks
while not passwordvalid:
    password1 = input("Please enter your password")
    password2 = input("Please re-enter your password")

    #Checks that the password matches
    if password1 != password2:
       print("The passwords do not match! :( \n Please try again.")

    #Checks if the password is between 8 and 12 characters long
    elif not (8 <= len(password1) <= 12):
        print("Your password is not within the specified range of between 8 and 12 characters.")

    #Checks for bad passwords (from the specified list)
    elif password1 in badpasswords:
        print("Bad password!!!!!")
    else:
        print("Password set!")
        passwordvalid = True