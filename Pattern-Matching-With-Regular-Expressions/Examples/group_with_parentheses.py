import re


# separating area code from rest of number with parentheses

phoneNum = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

message = input("Please enter a message for Dr. Pickle Bottom!: ")

mo = phoneNum.search(message)

if mo is None:
    print("No number found in message")
else:
    print(f"Number Part 1: {mo.group(1)}")
    print(f"Number Part 2: {mo.group(2)}")
    print(f"Number Part 3: {mo.group(3)}")
