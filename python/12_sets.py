# Set
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are written with curly brackets.
thisset={"apple","banana","cherry"}
print(thisset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
a={"apple","banana","apple","cherry"}
print(a)
print(len(a)) #o determine how many items a set has, use the len() function.

# Set Items - Data Types : Set items can be of any data type:
set1={"hello",False,20,5.3,}
print(set1)
print(type(set1))

# The set() Constructor : It is also possible to use the set() constructor to make a set.
set2=set(("apple","banana","cherry")) # note the double round-brackets
print(set2)

# Check if "banana" is present in the set:
set3={"apple","banana","cherry"}

tropical={"kiwi","watermelon"} #To add items from another set into the current set, use the update() method.
set3.update(tropical)
print(set3)

set3.add("orange") #To add one item to a set use the add() method.
# set3.add([4:5])  # Cannot add list or dictionary to sets
print(set3)

mylist=["strawberry","grapes"] #The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
set3.update(mylist)
print(set3)

print("banana" in set3 )

#Remove Item : To remove an item in a set, use the remove(), or the discard() method.

# If the item to remove does not exist, remove() will raise an error.and discard() will NOT raise an error.

set4 = {"apple", "banana", "cherry","kiwi","watermelon","strawberry","grapes"}
set4.remove("apple") #emove "apple" by using the remove() method:
# set4.remove(125) #throws an error while trying to remove 125 (which is not present in the set)
print(set4)


set4.discard("banana") #Remove "banana" by using the discard() method:
print(set4)

# print(set4.pop()) # another way
x=set4.pop() #Remove a random item by using the pop() method:
print(x)

set4.clear() #The clear() method empties the set:
print(set4)

# set5 = {"apple", "banana", "cherry"}
# del set5 #The del keyword will delete the set completely:
# print(set5) #this will raise an error because the set no longer exists


# Join Two Sets
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set6 = {"a", "b" , "c"}
set7 = {1, 2, 3,4}

set8 = set6.union(set7) #The union() method returns a new set with all items from both sets:
print(set8)

set6.update(set7)  #The update() method inserts the items in set7 into set6:
print(set6)


# Keep ONLY the Duplicates
i = {"apple", "banana", "cherry"}
j = {"google", "microsoft", "apple"}

i.intersection_update(j) #The intersection_update() method will keep only the items that are present in both sets.
print(i)

k = i.intersection(j) #The intersection() method will return a new set, that only contains the items that are present in both sets.
print(k)

#Keep All, But NOT the Duplicates
l = {"apple", "banana", "cherry"}
m = {"google", "microsoft", "apple"}

l.symmetric_difference_update(m) # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print(l)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y) #The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
print(z)

# Important: This syntax will create an empty dictionary and not an empty set
n = {}
print(type(n))

# An empty set can be created using the below syntax:
o = set()
print(type(o))

# Adding values to an empty set
p=set()  #Creating an empty set
print(type(p))

#Adding values to an empty set
p.add(4)
p.add(4)
p.add(5)  #Adding value repeadted does not changes a set
p.add(5)
p.add((14,25,36))
print(p)

'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()       	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()                  	Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()      	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others

'''
