from math import log2
result = log2(1024)
print(result)

def displayTwice(msg):
    """This function is designed to display the variable msg twice."""
    print(msg)
    print(msg)
msg = "This message is so good, it's going to print twice!!!"
displayTwice(msg)

help(displayTwice)


a = input("Enter a value for a")
b = input("Enter a value for b")
def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
	    max = a
    else:
	    max = b
    return max
print(f'{findMax(a,b)}')

