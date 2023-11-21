if __name__ == '__main__':
    file = open("info.txt")
for line in file:
    print(line)
file.close()

file = open("info.txt", "a")
file = file.write("this is an extra line")
print(file)
file.close()


