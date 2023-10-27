#!/usr/bin/env python3

if __name__ == '__main__':
    import math
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

hypot = lambda a,b : math.sqrt(a * a + b * b)
print(type(hypot))

to_seconds = lambda hours,minutes = 0: (hours * 60 + minutes) * 60
print(f'{to_seconds(hours = 0,minutes = 2)}')
print(f'{to_seconds(hours = 2,minutes = 0)}')
print(f'{to_seconds(hours = 1,minutes = 30)}')

print(f'{to_seconds(1)}')