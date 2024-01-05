# Write a program  to open three files 1.txt,2.txt and 3.txt. If any of these files are not present a message without exiting the program must be printed prompting the same.
def readfile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read()) 
    except FileNotFoundError:
        print(f"File {filename} is not found")        
readfile("1.txt")
readfile("2.txt")
readfile("3.txt")

# Wrtie a program to print third,fifth and seventh element from a list using enumerate function
l = [1,2,3,4,5,6,7,8,9,10]
for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        # print(index,item)
        print(f"The {index + 1}th element is {item}")

# Write a list compreshion to print a list which contains the multiplication table of a user entered number.
num = int(input("Enter your number: "))
table = [num*i for i in range(1,11)]
print(table)

# Write a program to display a/b where a and b are integers. If b=0,display infinite by handling the ZeroDivisionError.
'''
a = int(input("Enter number a: "))
a = int(input("Enter number b: "))
try:
    print(a/b)
except:
    print("Infinite")
'''
# Store the multiplication tables generated in problem 3 in a file named table.txt
num1 = int(input("Enter your number: "))
table1 = [num1*j for j in range(1,11)]
print(table1)
with open("table.txt","a") as f:
    f.write(str(table1))
    f.write('\n')