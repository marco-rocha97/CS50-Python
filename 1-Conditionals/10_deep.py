# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
x = input("Input: ")
x = x.lower().replace("-", " ").strip()

if x == '42':
    print("Yes")
elif x == 'forty two':
    print("yes")
else:
    print("No")