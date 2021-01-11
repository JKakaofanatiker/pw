import secrets
import string
from colorama import Fore # needed for color
import pyperclip

print(Fore.GREEN + "Enter password length:") # tell the user to type the length of the password
length = input() # user input
length = int(length)
chars = string.digits + string.ascii_letters + string.punctuation # possible chars
print(Fore.RED + "Here is your password:")
# print(''.join(secrets.choice(chars) for _ in range(length))) # prints password
password = ''.join(secrets.choice(chars) for _ in range(length))
print(password)
pyperclip.copy(password)