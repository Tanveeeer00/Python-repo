# W#School Notes

# MAP()
# Definition and Usage
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax
# map(function, iterables)

# Parameter Values
# Parameter	Description
# function	Required. The function to execute for each item
# iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

def func(a,b):
    return a + b
x=map(func,("apple" , "banana" , "cherry"),(" orange" , " lemon" , " pineapple"))
print(list(x))


# FILTER()

# Definition and Usage
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

# Syntax
# filter(function, iterable)

# Parameter Values
# Parameter	    Description
# function	    A Function to be run for each item in the iterable
# iterable	    The iterable to be filtered

ages = [5, 12, 17, 18, 24, 32]
def myfunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myfunc,ages)
for y in adults:
    print(y)






# Harry Notes

# MAP

def squ(num):
    return num*num
l = [1,4,6]

# method 1
l2 = []
for item in l:
    l2.append(squ(item))
print(l2)

# Method 2
l3 = map(squ, l)
print(list(l3))


# FILTER

# Filter Syntax: list(filter(function, list))

def greater_than_5(num1):
    if num1 > 5:
        return True
    else:
        return False
    
g4 = lambda num2:num2>10

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]

print(list(filter(greater_than_5,l4)))
print(list(filter(g4,l4)))

# Reduce

# Reduce applies a rolling computation to sequential pair of elements 

# Reduce Syntax : reduce(function,list)

from functools import reduce
sum = lambda a,b : a + b
lis = [1,2,3,4]
val= reduce(sum,lis)
print(val)
