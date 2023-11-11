if __name__ == '__main__':

    names = [ "Eric", "anna", "Sophie", "sam" ]
names.sort()
print(names)

names = sorted(names, key=lambda s: s.lower())
print(names)

colours = ["red", "green", "yellow", "blue", "red"]
print(colours.index("blue"))
print("Original list" , colours)
newcolours = colours.copy()
colours.extend(["pink, maroon, silver"])
print("Colours list that has been modified" , colours)
print("The copied list" , newcolours)

#this is not where I live btw, it probably isn't even a real place.
address = "458", "Northumbria Grove", "SK63 9DL"
print(address)

house_num = (address[0])
street = (address[1])
postcode = (address[2])
print(house_num)
print(street)
print(postcode)


empty = ()
the_one = "Neo",
the_onev = ("Neo")

print(type(empty))
print(type(the_one))
print(type(the_onev))