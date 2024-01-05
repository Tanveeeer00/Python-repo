'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
'''
# syntax of dictionary
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)

'''
Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''

a={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(a["brand"])

'''
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
'''
b={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020  #Duplicate values will overwrite existing values:
}

print(b)

# Add another dictionary , list and change value

c={
    "fast":"In a Quick Manner",
    "Tanveer":"he is a boy",
    "marks":[1,2,5],
    "anotherdict":{'Tanveer':'player'},
    1:2
}

print(c)

print(c['fast']) #You can access the items of a dictionary by referring to its key name, inside square brackets:

print(c['Tanveer'])


c["marks"]=[45,78]

print (c["marks"])

print(c["anotherdict"]["Tanveer"])

print(list(c.keys()))

print(c.keys()) # Prints the keys of the dictionary

print(c.values())  # Prints the keys of the dictionary 

print(c.items()) # Prints the (key, value) for all contents of the dictionary

print(c)

updatedict={
    "lovish":"friend",
    "Divya":"friend",
    "Shubham":"friend",
    "Harry":"A Dancer"
}
c.update(updatedict)  # Updates the dictionary by adding key-value pairs from updateDict
print(c)

c["color"]= "red" # Adding an item to the dictionary is done by using a new index key and assigning a value to it:
print(c)

c.pop("fast") # he pop() method removes the item with the specified key name:
print(c)

c.popitem() #The popitem() method removes the last inserted item 
print(c)


print(c.get("Tanveer")) # Prints value associated with key "harry"
print(c["Tanveer"]) # Prints value associated with key "harry"


# The difference between .get and [] sytax in Dictionaries?
print(c.get("Tanveer2"))  # Returns None as harry2 is not present in the dictionary
# print(c["Tanveer2"])         # throws an error as harry2 is not present in the dictionary


# Dictionary Length : To determine how many items a dictionary has, use the len() function:
print(len(c)) #Print the number of items in the dictionary:

c.clear() #The clear() method empties the dictionary:
print(c)

# del c #this will raise an error because the set no longer exists
# print(c)

# Dictionary Items - Data Types : The values in dictionary items can be of any data type:
d = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(d)

print(type(d))  #Type()


# The dict() Constructor : It is also possible to use the dict() constructor to make a dictionary.
e = dict(name="Tanveer",age=21,country="Japan")
print(e)
print(e.keys())
print(e.values())
print(e.items())


# Changing : Make a change in the original dictionary, and see that the items list gets updated as well:
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

# keys()
f=car.keys()
# print(f)
car["color"]="white"
print(f)

# values()
g=car.values()
car["year"]=2020
print(g)

# items()
h=car.items()
car["engine"]=2002665
print(h)

if "model" in car:
    print("yes,'model'is one of the keys in tehe car dictionary")

# Copy a Dictionary
i = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
j=i.copy() #Make a copy of a dictionary with the copy() method:
print(j)

k=dict(i) #Make a copy of a dictionary with the dict() function:
print(k)

# Nested Dictionaries : A dictionary can contain dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily={
    "child1":{
    "name":"yuri",
    "age": 16
},
"child2":{
"name":"tan",
    "age": 25
},
    "child3":{
    "name":"bon",
    "age": 26
}
}
print(myfamily)

# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(family)

'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	                        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

'''
































































