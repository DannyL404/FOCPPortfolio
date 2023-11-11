if __name__ == '__main__':
    import math

squares = [4, 9, 16, 25]
squarednums = [ ]

squares.append(49)
squares.append(64)
squares.append(81)

squares.extend([121, 144, 169])

squares.insert(0, 2)

squares.remove(49)
poppedvalue = squares.pop(0)
print(poppedvalue)
print(squares)

squares.reverse()
print(squares)

for x in squares:
    squarednums.append(math.sqrt(x))
print(squarednums)

squares = [x * x * x for x in squares]
print(squares)

newlist = [1, 2, 3, 1, 2]
newlist.remove(2)
print(newlist)