import random


numb = random.randint(1,100)

while True:
    guess = int(input("Enter your guess: "))
    if guess < numb:
        print("Number is greater than your guess")
    elif guess > numb:
        print("number is less than your guess")
    else: 
        print("You have guessed correctly. ")
