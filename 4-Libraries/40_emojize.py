# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
import emoji

emoji_code = input("input: ")

print("Output:", emoji.emojize(emoji_code, language="alias"))