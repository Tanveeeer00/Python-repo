# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Creating a tuple using ()
t=(1,2,4,5)
# t1=()       #Empty tuple
# t1=(1)      #Wrong way to declare a tuple with single element
print(t)

t1=(1,)       #tuple with single element
print(t1)

# printing the elements of a tuple
print(t[0])

# Cannot update the values of a tuple
# t[0] = 34   # throws an error

# Creating a tuple using ()
t2 = (1, 2, 4, 5, 4, 1, 2,1 ,1,3)
print(t2.count(1))
print(t2.index(3))

tl=("apple","banana","cherry",2,True,2.56)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
print(len(tl))

# A tuple can contain different data types:
print(tl)

# TYPE()
#  tuples are defined as objects with the data type 'tuple':
print(type(tl))

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
print(tl[1])

# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
print(tl[-1])


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
print(tl[2:5])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)
print(tl[-4:-1])

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


'''
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Change value, Add Item, Remove Item
'''
x=("apple","orange","cherry")
y=list(x)
y[1]="banana"
y.append("mango")
y.remove("apple")
x=tuple(y)
print(x)


# update() item
# method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#  the discard method to remove "banana" from the fruits set.
fruits1 = {"apple", "banana", "cherry"}
fruits1.discard("banana")
print(fruits1)

#  JOIN SETS

# Note: Both union() and update() will exclude any duplicate items.

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set_1 = {"a", "b" , "c"}
set_2 = {1, 2, 3}

set_1.update(set_2)
print(set_1)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Return a set that contains the items that exist in both set x, and set y:
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z1 = x1.intersection(y1)

print(z1)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x2.symmetric_difference_update(y2)

print(x2)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}

z3 = x3.symmetric_difference(y3)

print(z3)

'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	                         Adds an element to the set
clear()                        Removes all the elements from the set
copy()	                       Returns a copy of the set
difference()	                 Returns a set containing the difference between two or more sets
difference_update()            Removes the items in this set that are also included in another, specified set
discard()                      Remove the specified item
intersection()	               Returns a set, that is the intersection of two other sets
intersection_update()          Removes the items in this set that are not present in other, specified set(s)
isdisjoint()                   Returns whether two sets have a intersection or not
issubset()	                   Returns whether another set contains this set or not
issuperset()	                 Returns whether this set contains another set or not
pop()	                         Removes an element from the set
remove()	                     Removes the specified element
symmetric_difference()	       Returns a set with the symmetric differences of two sets
symmetric_difference_update()	 inserts the symmetric differences from this set and another
union()	                       Return a set containing the union of sets
update()	                     Update the set with the union of this set and others
'''