if __name__ == '__main__':
    import math

w = 104.32
h = 15.654
print(f"A cricle with width {w} and height {h} has an area of {h * w:.3f}")

names = "Serena"
age = 29
print(f"{names:15} - {age:10}")
names = "Blair"
age = 31.5765
print(f"{names:15} - {age:10}")

print(f"{names:$>20} - {age:$>20.2}")

r = 52
area = r * r * math.pi
print("A circle with radius {} has an area of {}".format(r,area))

name = "Darota"
age = 450
print("{name:@^15} - {age:#^10}".format(name=name, age=age))


