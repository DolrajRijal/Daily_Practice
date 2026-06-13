import random
import string
len = int(input("Enter the length of the password"))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(len):
    password += random.choice(characters)
    # print(password)

print(f"password is {password}")
# print(len(string.punctuation))