
# Write a program using function to find greatest of three numbers
def maximum(num1,num2,num3):
        if(num1>num2):
            if(num1>num3):
                return num1
            else:
                return num3
        else:
            if(num2>num3):
                return num2
            else:
                return num3
m = maximum(23,65,47)
print("The maximum value is " + str(m))


# Write a python program using function to convert celsius to degree
def deg(cel):
    return (cel * (9/5)) + 32 
celc=deg(5)
print(celc)

 
# How do you prevent a python print() function to print a new line at the end.
print("Hello,",end=" \n") #end= is built in function
print("how",end=" ")
print("are",end=" ")
print("you?",end=" ")


# Write a recursive function to calculate the sum of first n natural numbers
def mySum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+mySum(n-1)
natural=mySum(5)
print(natural)

# Write a python function to print first n lines of the following pattern
q=3
for i in range(q):
    print("*"*(q-i)) #prints * n-1 times

    
# Write a python function which converts inches to cms

def centi(cm):
    return (cm*2.54)
centimeter=centi(5)
print(centimeter)

# Write a pythin function to remove a given word from a list and strip it at the same time 
this=("    harry   ")
print(this)                   #this is a strip example
print(this.strip())

def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
that="   this ia a good boy   "
t = remove_and_split(that,"this")
print(t)

# Write a python function to print multiplication table of a given number
def table(w):
    for u in range(1,11):
        print(w ,"x" ,u ,"=" ,w*u)
# v= table(2)
# print(v)
w = int(input("Enter your number\n"))
table(w)

# Write a program using function to find greatest of four numbers
def mini(num1,num2,num3,num4):
    if(num1>num2 and num1>num3 and num1>num4):
        return num1
    elif(num2>num1 and num2>num3 and num2>num4):
        return num2
    elif(num3>num1 and num3>num2 and num3>num4):
        return num3
    else:
        return num4
maxi=mini(65,98,45,79)
print(maxi)