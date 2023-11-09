if __name__ == '__main__':

#This is importing the system variable. This variable provides various functions and variables that interact strongly with the interpreter.
	import sys

#This is a lsit of anything in the command line and after the program name. It is ALWAYS strings.
count = len(sys.argv)
total = 0
average = 0
#This loop runs through the list of values input and then divides it by 3 to calculate an average
while count > 1:
	count -= 1
	total += float(sys.argv[count])
	average = total
	average = average / 3

#If no values are input then this code will run
if total == 0:
	print("No arguments were provided")
#If values are entered then it will return these values.
else:
	print("Total is", total)
	print("Average is", average)