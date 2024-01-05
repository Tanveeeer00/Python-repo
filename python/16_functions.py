# w3wschool notes

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# Creating a Function
# In Python a function is defined using the def keyword:
def my_function():
    print("hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()

# Arguments
# Information can be passed into functions as arguments.Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
# parentheses = ()
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function2(fname1, lname1):
  print(fname1 + " " + lname1)
my_function2("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.This way the function will receive a tuple of arguments, and can access the items accordingly:
# If the number of arguments is unknown, add a * before the parameter name:
def my_function3(*kids):
  print("The youngest child is " + kids[2])
my_function3("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.
def my_function4(child3, child2, child1):
  print("The youngest child is " + child2)
my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.This way the function will receive a dictionary of arguments, and can access the items accordingly:
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function5(**kid1):
  print("His last name is " + kid1["lname2"])
my_function5(fname2 = "Tobias", lname2 = "Refsnes")

# Default Parameter Value
# The following example shows how to use a default parameter value.If we call the function without argument, it uses the default value:
def my_function6(country = "Norway"):
  print("I am from " + country)
my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function7(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function7(fruits)

# Return Values
# To let a function return a value, use the return statement:
def my_function8(x):
  return 5 * x
print(my_function8(3))
print(my_function8(5))
print(my_function8(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction9():
  pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Arguments are often shortened to args
# Arbitrary Arguments are often shortened to *args
# The phrase Keyword Arguments are often shortened to kwargs
# Arbitrary Kword Arguments are often shortened to **kwargs 

# code with harry notes 
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400 )*100
    return p
marks1 = [45,65,84,95]
percentage1 = percent(marks1)

marks2 = [22,94,62,47]
percentage2=percent(marks2)
print(percentage1,percentage2)

# quick quiz
def greet(name):
    print("Good day, " + name)
greet("harry")

def mySum(num1,num2):
    return num1+num2
# a = 12
# b = 15
# c = mySum(a,b)
# print(c)
s = mySum(12,15)
print(s)

# Default argument
def defa(name="stranger"):
    print("Good day, "+ name)
defa("Harry")
defa()

# factorial in loop,function,recursive
# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)! 
# loop
n=5
product=1
for i in range(n): 
    product = product*(i+1)
print(product)

# function
def factorial_inter(m):
    pro = 1
    for j in range(m):
        pro=pro*(j+1)
    return pro
# print(factorial_inter(4))
f = factorial_inter(4) #other way to print
print(f)

# recursive
def factorial_recursive(p):
    if p == 1 or p==0:
      return 1
    else:
      return p* factorial_recursive(p-1)
g = factorial_recursive(6)
print(g)


# LAMBDA
# W#School notes
# A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression. 
# Use lambda functions when an anonymous function is required for a short period of time.

# lambda arguments : expression         #The expression is executed and the result is returned:

ab = lambda bc : bc + 10
print(ab(10))

ba = lambda cb,dc : cb * dc    #Lambda functions can take any number of arguments:
print(ba(5,6))

m = lambda ef,fg,gh : ef + fg + gh
print(m(2,6,4))

def funcy(n):
  return lambda a : a * n
mydoubler = funcy(5)
print(mydoubler(2))

def funcy1(q):
  return lambda a : a * q
mydoubler1 = funcy1(10)
mydoubler2 = funcy1(20)
print(mydoubler1(10))
print(mydoubler2(15))


# Harry Notes

'''
def funcy2(a):
   return a + 5
my = funcy2(5)
print(my)
'''
funcy3 = lambda a : a + 5
print(funcy3(15))

funcy4 = lambda a : a + 5
squa = lambda a : a * 2
sum = lambda a,b,c : a + 5 + 15
x = 3
print(funcy4(x))
print(squa(x))
print(sum(x,2,3))