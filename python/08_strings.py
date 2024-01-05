a = "Tanveer"
# a = "Tanveer's"         # --> Use this if you have single quotes in your strings
# a = 'Tanveer"s'
# a = '''Tanveer's and
#        Tanveer"s'''
print(a)
print(type(a))

# Concatenating two strings
greeting = "Good Morning, "
name = "Tanveer"
b = greeting + name
print(b)

# string slicing

#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

# index start from 0 and it's including but last number are excluding.

naam = "Tanveer"
print(naam[4])
print(naam[1:4])
print(naam[:4])      # is same as name[0:4]
print(naam[1:])      # is same as name[1:5]

# negative indices. (its start with -1 from last)
c = naam[-4:-1] #is same is name [1:4]
print(c)

name="TanveerisGood"
d = name[0:10:3]  #0 is initial , 10 is end point and 3 is how much want slice
d = name[0::2]
d = name[:0:-1]
print(d)

# string function

story = "once upon a time there was a youtuber named harry who uploaded python course with harry notes "
# length
print(len(story))
# check end by boolean
print(story.endswith("notes"))
print(story.endswith("harry"))
# count words and alphabet
print(story.count("c"))
# capitalize
print(story.capitalize())
# find
print(story.find("upon"))
# replace
print(story.replace("harry","Tanveer"))
# uppercase
print(story.upper())
# lowercase
print(story.lower())
# removes whitespace from start and end
print(story.strip())
# split
print(story.split("harry"))

#Format strings
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} 
age = 36
txt = "my name is tanveer,and i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# we can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantities = 5
itemnos = 2
prices = 65.23
order = "I want to pay {2} dollars for {0} pieces of item {1}. "
print(order.format(quantities,itemnos,prices))

# Escape Characters
e = "hello,\tmy name is \\tanveer\\.\nIt\'s also  \bcalled luffy "
print(e)

# JOIM
l=["Camera","laptop","Phone","ipad","Hard Disk","Nvidia","Graphic card"]
sentence = "\n".join(l)
sentence1 = " == ".join(l)
sentence2 = " and ".join(l)
print(sentence)
print(sentence1)
print(sentence2)

'''
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	                       Description
capitalize()           	Converts the first character to upper case
casefold()	            Converts string into lower case
center()	            Returns a centered string
count()                 Returns the number of times a specified value occurs in a string
encode()	            Returns an encoded version of the string
endswith()          	Returns true if the string ends with the specified value
expandtabs()	        Sets the tab size of the string
find()              	Searches the string for a specified value and returns the position of where it was found
format()	            Formats specified values in a string
format_map()	        Formats specified values in a string
index()                 Searches the string for a specified value and returns the position of where it was found
isalnum()	            Returns True if all characters in the string are alphanumeric
isalpha()	            Returns True if all characters in the string are in the alphabet
isdecimal()	            Returns True if all characters in the string are decimals
isdigit()	            Returns True if all characters in the string are digits
isidentifier()	        Returns True if the string is an identifier
islower()	            Returns True if all characters in the string are lower case
isnumeric()	            Returns True if all characters in the string are numeric
isprintable()	        Returns True if all characters in the string are printable
isspace()	            Returns True if all characters in the string are whitespaces
istitle()	            Returns True if the string follows the rules of a title
isupper()	            Returns True if all characters in the string are upper case
join()	                Joins the elements of an iterable to the end of the string
ljust()	                Returns a left justified version of the string
lower()	                Converts a string into lower case
lstrip()	            Returns a left trim version of the string
maketrans()	            Returns a translation table to be used in translations
partition()	            Returns a tuple where the string is parted into three parts
replace()	            Returns a string where a specified value is replaced with a specified value
rfind()	                Searches the string for a specified value and returns the last position of where it was found
rindex()	            Searches the string for a specified value and returns the last position of where it was found
rjust()	                Returns a right justified version of the string
rpartition()	        Returns a tuple where the string is parted into three parts
rsplit()	            Splits the string at the specified separator, and returns a list
rstrip()	            Returns a right trim version of the string
split()	                Splits the string at the specified separator, and returns a list
splitlines()	        Splits the string at line breaks and returns a list
startswith()	        Returns true if the string starts with the specified value
strip()	                Returns a trimmed version of the string
swapcase()	            Swaps cases, lower case becomes upper case and vice versa
title()	                Converts the first character of each word to upper case
translate()	            Returns a translated string
upper()	                Converts a string into upper case
zfill()	                Fills the string with a specified number of 0 values at the beginning
'''