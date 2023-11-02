#This is a file that Asks a user for a number, it will then return it and if it is an odd or an event number.

#This is taking a number input for the user
number = input("Enter a number: ")
#This converts the imported text as a number
number = int(number)

#This displays the entered number
print("The numbered entered was", number)

#This divides the number leaving just the remainder. If a number is even (divisible by two) this will be 0.
if (number % 2) == 0 and (number % 10) == 0:
	print("That is an even number and also a multiple of 10.")
elif (number % 2) == 0:
        print("This is an even number")
else:
	print("That is an odd number")
