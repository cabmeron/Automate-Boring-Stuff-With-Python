import re

# basic american number regex


# creating regex object
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


# matching regex object (mo = match object)

message = input("Please enter your message for Dr. Pickle Bottom: ")

mo = phoneNum.search(message)

if mo is None:
    print("No phone number found in message!")
else:
    print(f'Phone number: {mo.group()}')

    """
    Main steps for Regular Expressions in Python
    
    1) Import regex module: "import re"
    2) Create a regex obect with re.compile() function. (Remember to use a raw string)
    3) Pass the string you want to search into the Regex object's search() method. This returns a Match object
    4) Call the Match object's group() method to return a string og the actual matched text
    
    
    ***ALSO*** : pythex for showing exactly how a regex matches a piece of text that you entet
    
    """
