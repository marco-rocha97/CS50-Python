# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
a = 50
while a > 0:
    print(f"Amount Due: {a}")
    i = int(input("Insert Coin: "))
    if i == 5 or i == 10 or i == 25:
        a = a - i

a = abs(a)
print(f"Change Owed: {a}")