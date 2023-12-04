# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    try:
        m, d, y = date.split("/")

        m = int(m)
        d = int(d)
        y = int(y)

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02}-{d:02}")
            break

    except:
        try:
            m, d, y = date.split(" ")

            if d[len(d)-1] == ",":
                d = d.replace(",", "")
                d = int(d)

            if m in months and 1 <= d <= 31:
                for i in range(len(months)):
                    if m == months[i]:
                        m = i + 1
                        print(f"{y}-{m:02}-{d:02}")
                        break
                break

        except:
            pass