import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for char in range(1, nr_letters + 1):
    randc = random.choice(letters)
    password.append(randc)

for num in range(1, nr_numbers + 1):
    randn = random.choice(numbers)
    password.append(randn)

for sym in range(1, nr_symbols + 1):
    rands = random.choice(symbols)
    password.append(rands)

print("Before shuffle:", password)
random.shuffle(password)
print("After shuffle:", password)

f_password = ""
for char in password:
    f_password += char

print(f"Your password is: {f_password}")
