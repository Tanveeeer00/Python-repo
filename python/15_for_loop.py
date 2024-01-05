# The for loop does not require an indexing variable to set beforehand.
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# for list loop

fruits = ["apple","banana","cherry"]
for a in fruits:
    print(a)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
for i in "banana":
    print(i)

# Range function 
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note that range(10) is not the values of 0 to 10, but the values 0 to 9.
for b in range(10):
    print(b)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(5,12), which means values from 5 to 12 (but not including 12):
for c in range(5,12):
    print(c)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(4, 20, 2):
# Increment the sequence with 2 (default is 1):
for d in range(4,20,2):
    print(d)

# else statement
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 9, and print a message when the loop has ended:
# The else block will NOT be executed if the loop is stopped by a break statement.
for e in range(10):
    print(e)
else:
    print('this is inside else of for')
    
# break statement
# With the break statement we can stop the loop before it has looped through all the items:
for f in range(10):
    print(f)
    if f==5:
      break
else:
    print("this is inside of for")

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# continue statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

for g in range(10):
    if g == 5:
        continue
    print(g)

# pass statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
h = 4
def run(player):
    pass
def ouch(player):
    pass
if h>0:
    pass
while h>6:
    pass
print("Tanveer is a good boy")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
j = ["red","big","tasty"]
k = ["apple","orange","banana","cherry"]
for x in j:
    for y in k:
        print(x,y)