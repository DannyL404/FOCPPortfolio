#!/usr/bin/env python3

if __name__ == '__main__':
    age = 19

print(18 < age)
print(21 < age)
print(31 < age)

age = 30

age >=18 and age <=65
age <18 or age >65
not age > 18

print(age)

age = 30

(age >=18 and age <=65) and (not age==30)

print(age)

#Membership testing excersise
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("James" in names)
print("Mark" not in names)

message = "Hello there, my name is John"
print("ham" in message)

age = int(input("please enter your age"))
if 18 < age < 30:
    print("you are still young")
elif 29 < age < 40:
    print("You are mildly old (middle aged era)")

name = input("Please enter your name")
if name == "Dan":
    print("Hello Dan")
else:
    print("No authorisation, poor choice of name")

child = 0
adult = age if age >= 18 else child

for n in ["James", "Dan", "Mia", "Charlotte"]:
    print(n)

for n in range(2, 11, +2):
    print(n, "to the power of", n , "is" , n * n)