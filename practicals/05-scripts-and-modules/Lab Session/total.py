if __name__ == '__main__':

import sys

count = len(sys.argv)
total = 0
average = 0
while count > 1:
	count -= 1
	total += float(sys.argv[count])
	average = total
	average = average / 3

if count == 0:
	print("No arguments were provided")

else:
	print("Total is", total)
	print("Average is", average)