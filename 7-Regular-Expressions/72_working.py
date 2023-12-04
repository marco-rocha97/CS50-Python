# In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
# Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
# But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"([0-9]+)(?:(?::)([0-9]+))? (AM|PM) to ([0-9]+)(?:(?::)([0-9]+))? (AM|PM)", s, re.IGNORECASE):
        h_1 = int(matches.group(1))
        h_2 = int(matches.group(4))

        if h_1 > 12 or h_2 > 12:
            raise ValueError

        if h_1 == 12:
            h_1 = 0
        if h_2 == 12:
            h_2 = 0

        if matches.group(2) != None:
            m_1 = int(matches.group(2))
            if m_1 >= 60:
                raise ValueError
        else:
            m_1 = 0
        if matches.group(5) != None:
            m_2 = int(matches.group(5))
            if m_2 >= 60:
                raise ValueError
        else:
            m_2 = 0

        if matches.group(3) == "AM":
            return f"{h_1:02}"+":"+f"{m_1:02}"+" to "+f"{h_2+12:02}"+":"+f"{m_2:02}"
        else:
            return f"{h_1+12:02}"+":"+f"{m_1:02}"+" to "+f"{h_2:02}"+":"+f"{m_2:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()