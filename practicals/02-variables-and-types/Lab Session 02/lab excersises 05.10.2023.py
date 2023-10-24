total = 100

print('The total is' , total)

total = total + 99

print('The total is' , total)

total -= 1
print('the total is' , total)

total *= 4
print('the total is' , total)

total /= 2
print('the total is' , total)

total = 98.2
count = 5
average = total / count
print(average)

print("ABC" * 10)


print(len("Dan"))

age = input("What is your age?")
age = int(age)
print("In one year your age will be, " , age + 1)

num1 = input("Please enter your first number")
num1 = int(num1)
num2 = input("Please enter your second number")
num2 = int(num2)
print(num1 * num2)

print("This text includes characters such as '\' '"' and "'", \n\t This is a new line that starts with a tab \n\t\t This new line starts with two tabs")

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \nHello there! \n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print("""This text spans three lines, 
and includes both single (')
and double quotes (")""")

surname = "Liles"
initial = surname[-1]
print(initial)

surname = "Liles"
middle = surname[1:]
print(middle)

primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(primes[:4])

names = ["Tim", "Bill", "Graeme"]
names.append("James")
names.append("Dave")
print(names)
