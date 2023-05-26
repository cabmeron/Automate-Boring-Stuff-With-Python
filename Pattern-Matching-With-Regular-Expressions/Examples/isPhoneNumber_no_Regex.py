# Author: Cabmeron
# Date: 05/26/2023
# Description: Finding phone number (American) pattern in provided string without regular expressions
# ###-###-#### (10 numbers, 2 hyphens (12 char))

def isPhoneNumber(text):

    # len of number should be 12 characters at minimum
    if len(text) != 12:
        return False

    # logic to check for sequential order of numbers and hyphens that represent a proper american number

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

# Extracting phone number from a provided message


def main():

    message_number = ""
    number_exists_in_message = False
    message = input("Please provide your message here for Dr. PickleBottom!: ")

    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            number_exists_in_message = True
            message_number = chunk
            break

    if number_exists_in_message:
        print(f"Number found in message: {chunk}")
    else:
        print("No identiable number found in message")


if __name__ == "__main__":
    main()
