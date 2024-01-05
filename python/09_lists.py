'''Changeable.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.'''


# Create a list using []

a  = [1,2,4,56,6]

# print the list using print() function

print(a)

# Access using index using a[0], a[1], a[2]

print(a[2])

# Change the value of list using 

a[0] = 28
print(a)

# Change a Range of Item Values
a[1:3] = ["256","896"]
print(a)

# We can create a list with items of different types 

a = [1, "Tanveer", True, 2.68]
print(a)

# List Slicing 

friends= ["Tanveer", "Harry", "Tom", "rohan", "sam", "divya"]
print(friends[0:4])
print(friends[-4:])

# Sorts, Reverse, Append, Inserts, Pop, Remove

li=[1, 8, 7, 2, 21, 15]
print(li)

li.sort()          # sorts the list
print(li)
li.reverse()       # reverses the list
print(li)
li.append(45)      # adds 45 at the end of the list 
print(li)
li.insert(2,255)   # inserts 544 at index 2
print(li)
li.pop(2)          # removes element at index 2
print(li)
li.remove(21)      # removes 21 from the list
print(li)
#del li            # The del keyword can also delete the list completely.
del li[1]          # The del keyword also removes the specified index
print(li)
li.clear()       # The clear() method empties the list.The list still remains, but it has no content.

print(li)

# Allow Duplicate
# Since lists are indexed, lists can have items with the same value:

li_1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(li_1)

# List Length
# To determine how many items a list has, use the len() function:

print(len(li_1))
 

# List type 
#  lists are defined as objects with the data type 'list':

print(type(li_1))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

li_2 = list(("apple", "banana", "cherry"))
print(li_2)

# Check if Item Exists
# To determine if a specified item is present in a list use the "in" keyword:

li_3 = ["apple", "banana", "cherry", "grapes", "cherry"]
if "apple" in li_3:
    print("Yes,'apple' is in the fruits list")

# Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.). 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Copy a List
# Make a copy of a list with the copy() method:
thislist1 = ["apple", "banana", "cherry"]
mylist1 = thislist1.copy()
print(mylist1)
# Make a copy of a list with the list() method:
thislist2 = ["apple", "banana", "cherry"]
mylist2 = list(thislist2)
print(mylist2)

# count() Method
# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry','cherry']

x = fruits.count("cherry")
print(x)


'''
List Methods
Python has a set of built-in methods that you can use on lists.

Method	                Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()   	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''