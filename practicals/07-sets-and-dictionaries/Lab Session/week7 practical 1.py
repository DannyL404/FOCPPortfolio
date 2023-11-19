import math

names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)

sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
print(unique_letters)

name = input("Enter your name: ")
if name not in names:
	print("You are listed in the set of known names")


staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}
staff = staff.union({"Mark", "Ringo"})
print(staff)
staff = staff.intersection(staff & directors)
print(staff)
external = staff.difference(directors - staff)
print(staff)
stafforexternal = staff.symmetric_difference(directors)
print(stafforexternal)

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if staff <= managers:
    print("All managers are staff members")



stock = ["banana", "chocolate", "bread rolls", "Pasta", "Chicken nuggets", "Potatoes", "Crisps", "Lemonade", "Tomatoes", "Apples", "Oranges"]
stock[10] = "Kiwi"
print(stock)
stock.pop(0)
print(stock)

roots = {n : math.sqrt(n) for n in range(1,26)}

for n in roots.dict:
    print("The square root of", roots.keys(n), "is", roots.values(n))

print(roots)