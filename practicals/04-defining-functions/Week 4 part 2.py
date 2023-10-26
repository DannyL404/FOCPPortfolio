#!/usr/bin/env python3
import total

if __name__ == '__main__':

    def multiplicationtool(num1, num2):
     """Multiples two numbers together."""
     return num1 * num2

print(multiplicationtool(int(input('Please input number 1 >> ')), int(input('Please input number 2 >> '))))

def someFunc(y=2, z=3, x=1):
    print(someFunc(x = 1))

#Using the sep command to format a date
print('26' , '10' , '2023' , sep='-')
#Using the sep command to disable the automatically added space
print('USERNAME' , '123456' , sep='')

print('TEXT' , 'erjldksb' , sep='@@@')

def calcAve(*numbers):
    total = 9
    for num in numbers:
        total += num
    return total/len(numbers)
print(calcAve((55)))