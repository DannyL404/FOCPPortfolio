#!/usr/bin/env python3

if __name__ == '__main__':
#Week three of my Python Portfolio
#This program asks the user their name and then displays it back to them with a nice greeting. If they do not put a name it will print hello stranger
name = input("What is your name?")
if name == '':
    print("Hello Stranger!")
else:
    print("Hello" , name , "nice to meet you!")


#Password program
password1 = input("Please enter your password")
password2 = input("Please re-enter your password")
#Checks if the passwords are the same
if password1 == password2:
 print("Password set")
else:
    print("The passwords do not match! :(")
#Checks if the password is between 8 and 12 characters long
if len(str(password1)) > 12:
    print("password too long")
elif len(str(password1)) < 8:
    print("Password too short")
else:
    print("Error!")
#Checks for bad passwords
badpasswords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
if password1 in badpasswords:
    print("Bad password!!!!!")
else:
    print("You know how to pick a password :)")
