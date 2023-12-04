# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.
name = input("camelCase: ")

for c in name:
    if c.islower() == True:
        print(c, end="")
    else:
        c = c.lower()
        print(f"_{c}", end="")