# Harry Notes

'''
try:
    #code                           #code which might throw exception
except exception as e:
    print(e)                

try:
    #code
except ZeroDivisionError:
    #code
except TypeError:
    #code                           #All other exception are handled here
'''


while(True):
    print("Press q to quit")
    a = input("Enter a number :")
    if a == "q":
         break
    try:
         print("Trying....")
         a = int(a)
         if a>6:
              print("You entered a number greater than 6")
    except Exception as e:
         print(f"Your input resulted in an error: {e}")
print("Thanks for playing this game")


try:
    b = int(input("Enter Your Number: "))
    c = 1/b
    print(c)
except ValueError as e:
    print("Please Enter a valid value")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")
print("Thanks for using this code!")

def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Please enter valid number")
d = increment("df5")
print(d)

try:
    g = int(input("Enter a number: "))
    f = 1/g
except Exception as e:
    print(e)
else:
    print("we were successful")

try:
    j = int(input("Enter a number: "))
    k = 1/j
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")
print("Thanks for using the program")

# Global variable
r = 52            #Global variable
def func1():
    global r 
    print(f"print statement 1: {r}")
    r = 8         # Local Variable if global keyword is not used
    print(f"print statement 2: {r}")
func1()
print(f"print statement 3:{r}")

# enumerate
list1 =[3,54,59,85,14,51,32,76,96,42,84,64]
# index=0
# for item in list1:
#     print(item,index)
#     index +=1
for index,item in enumerate(list1):
    print(item,index)

# comprehension
m = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]

'''
n = []
for items in m:
    if items%2==0:
        n.append(items)
print(n)
'''

# Shortcut to write the same:
n=[items for items in m if items%2==0]
print(n)

o = [1,4,2,4,1,2,3]
p ={val for val in o}
print(p)


# W#School
'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
# TRY
# These exceptions can be handled using the try statement:

'''
try:                #The try block will generate an error, because ab is not defined:
  print(ab)         #Since the try block raises an error, the except block will be executed.Without the try block, the program will crash and raise an error:
except:
  print("An exception occurred")
'''

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# This can be useful to close objects and clean up resources:

'''
try:
  print(bc)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
'''
# Example
# Try to open and write to a file that is not writable:
# The program can continue, without leaving the file object open.

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.To throw (or raise) an exception, use the raise keyword
# The raise keyword is used to raise an exception.You can define what kind of error to raise, and the text to print to the user.
x = -1          #Raise an error and stop the program if x is lower than 0:
if x < 0:
  raise Exception("Sorry, no numbers below zero")