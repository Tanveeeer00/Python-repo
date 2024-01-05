
a = int(input("Enter the value: \n"))
# 1. if-elif-else ladder in python
if(a<3):
    print("The value",a, "is lesser than 3")
elif(a<7):
    print("The value",a, "is lesser than 7")
elif(a<13):
    print("The value",a, "is lesser than 13")
elif(a<20):
    print("The value",a, "is lesser than 20")
else:
    print("The value",a, "is greater than 3 or 7 ")
print("done")

# 2. Multiple if statements
b = int(input("Enter the value \n"))
if(b<3): 
    print("The value",b,"is greater than 3")

if(b>13):
    print("The value",b,"is greater than 13")
    
if(b>7):
    print("The value",b,"is greater than 7")

if(b>17):
    print("The value",b,"is greater than 17")
else:
    print("The value",b, "is not greater than 3 or 7")

print("Done")

# if-else quick quiz
age = int(input("Enter your age: "))
if(age>=18):
    print("YES")
else:
    print("NO")


# logical and relational operators

ages=int(input("Enter your age: "))
if(ages>34 and ages<56):
    print("you can work with us")
else:
    print("you cannot work with us")

aged=int(input("Enter your age: "))
if(aged>34 or aged<56):
    print("you can work with us")
else:
    print("you cannot work with us")

h = int(input("Enter the value: "))
if(h==7):
    print("yes")
elif(h<56):
    print("no and yes")
else:
    print("I am optional")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
c = 33
d = 200

if c > d:
  pass

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# IN and IS 
e = None
if(e is None):
    print("YES")
else:
    print("NO")

f = [45,56,6]
print(435 in f)
print(56 in f)

