# Write a program to display a user entered name followed by Good Afternoon using input() function

a = input("Enter your name:\n")
print("Good Afternoon, "+a)

# Write a program to fill in a letter template given below with name and date

letter = '''Dear <|Name|>
            you are selected!
            <|date|>'''

a = input("Enter your name:")
b = input("Enter date:")
letter=letter.replace("<|Name|>",a)
letter=letter.replace("<|date|>",b)
print(letter)

# Write a program to detect double space and replace with single single space

a = "hello everyone  i am tanveer  what about you" 
doublespace= a.find("  ")
print(doublespace)
a=a.replace("  "," ")
print(a)

# write a program to format the following letter using escape squence characters

in_letter= "Dear Tanveer,This python course is nice!Thanks"
print(in_letter)
formatted_letter="Dear Tanveer,\n\tThis python course is nice!\nThanks"
print(formatted_letter)

