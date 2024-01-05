
# Write a program to input name,marks and phone number of a student and format it using the format function like below
# "The name of the student is harry his marks are 72 and phone number is 99998888"

from functools import reduce
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))
template = "The name of the student is {}, his marks are {} and phone number is {}"
output = template.format(name, marks, phone)
print(output)

# A list contains the multiplication table of 7. Write a progran to convert it to a vertical string of same number
t = [str(i*7) for i in range(1, 11)]
print(t)
verticalTable = "\n".join(t)
print(verticalTable)

# Write a program to filter a list of numbers which are divisible by 5
l = [2, 5, 23, 25, 15, 45, 62, 56, 85, 31, 25, 12]
a = filter(lambda a: a % 5 == 0, l)
print(list(a))

# Write a program to find the maximum of the numbers in a list using the reduce function
lis = [2, 5, 6, 8, 54, 8, 4, 5]
b = reduce(max, lis)
print(b)
