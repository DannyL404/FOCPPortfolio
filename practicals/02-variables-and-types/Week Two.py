#Week two of my Python Portfolio

#This program asks the user their name and then displays it back to them with a nice greeting.
name = input("What is your name?")
print("Hello" , name , "nice to meet you!")

#This is a program that asks a user to enter a temperature in Celcius and then displays it back in Farenheit
celsiustemp = input("Please enter the temperature in Celsius.")
celsiustemp = float(celsiustemp)
fahrenheittemp = (1.8 * celsiustemp) + 32
print("The tempartature was" , celsiustemp , "in Celcius and is" , fahrenheittemp , "in Farenheit.")

#This is a program that asks how many students there are and the required group size. It will then calculate the number of full groups and the left over students.
students = input("Please enter the number of students.")
groupsize = input("Pleas enter the required group size.")
students = int(students)
groupsize = int(groupsize)
groups = students // groupsize
remainder = students % groupsize
print("There will be" , groups ," groups with" , remainder , "students left over.")

#This program is designed to allow a teacher to calculate how many sweets each student can have and how many will be left over to ensure an even number was distributed.
students = input("Please enter the number of students.")
sweets = input("Pleas enter the number of sweets")
students = int(students)
sweets = int(sweets)
studentsweets = sweets // students
remainder = sweets % students
print("Each student will receive" , studentsweets , " sweets and there will be" , remainder , "left over for the teacher." )