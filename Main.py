import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Hi ! Time to create your new random password!")
print("For the best result choose at least! 1 from each")

letterSelect = int(input("How many letters would you like in your password?\n"))

numberSelect = int(input("How many Numbers would you like?\n"))

symbolSelect = int(input("Okay, now how many symbols?\n"))

passwordList = []

for char in range(1 + letterSelect + 1):
    passwordList.append(random.choice(letters))  # using the range function, and passing the users inputs in a for loop.

for char in range(1 + numberSelect + 1):
    passwordList.append((random.choice(numbers)))   # The choice is added to the passwordList 'list'.

for char in range(1 + symbolSelect + 1):
    passwordList.append(random.choice(symbols))     # Then passed as a random choice of each.

password = ""
# The List is then passed as a char so it is more straight forward to print the users new password.
for char in passwordList:
    password += char

print(f"Your Brand new password is: {password}  KEEP IT SAFE! TELL NOBODY!")






