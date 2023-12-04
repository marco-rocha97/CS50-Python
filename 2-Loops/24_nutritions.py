# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. 
# Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). 
# Ignore any input that isn’t a fruit.
item = input("Item: ").lower()

fruits = [
    {"f": "apple", "c": "130"},
    {"f": "avocado", "c": "50"},
    {"f": "banana", "c": "110"},
    {"f": "cantaloupe", "c": "50"},
    {"f": "grapefruit", "c": "60"},
    {"f": "grapes", "c": "90"},
    {"f": "honeydew melon", "c": "50"},
    {"f": "kiwifruit", "c": "90"},
    {"f": "lemon", "c": "15"},
    {"f": "lime", "c": "20"},
    {"f": "nectarine", "c": "60"},
    {"f": "orange", "c": "80"},
    {"f": "peach", "c": "60"},
    {"f": "pear", "c": "100"},
    {"f": "pineapple", "c": "50"},
    {"f": "plums", "c": "70"},
    {"f": "strawberries", "c": "50"},
    {"f": "sweet cherries", "c": "100"},
    {"f": "tangerine", "c": "50"},
    {"f": "watermelon", "c": "80"},
]

for fruit in fruits:
    if item == fruit["f"]:
        f = fruit["c"]
        print(f"Calories: {f}")