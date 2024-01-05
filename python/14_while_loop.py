# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 10:
# Note: remember to increment i, or else the loop will continue forever.

i = 0
while i<10:
    print("yes" + str(i))
    i = i + 1
print("Done")

# Print i as long as i is equal than 10:
j = 1
while j <=50:
    print(j)
    j = j + 1

fruits=["banana","watermelon","grapes","mangoes"]
k = 0
while k < len(fruits):
    print(fruits[k])
    k = k + 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
l = 1
while l < 10:
    print(l)
    if l == 3:
        break
    l = l + 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
m = 0 
while m < 10:
    m += 1
    if m == 5:
        continue
    print(m)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
n = 1
while n < 10:
    print(n)
    n += 1 
else:
    print("n is no longer less than 10")