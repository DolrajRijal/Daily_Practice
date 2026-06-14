#rock paper scissor game
import random

options = ('rock', 'paper', 'scissor')
computer = random.choice(options)

player = None

running = True

while running:
    computer = random.choice(options)

    player = None
    while player not in options:
        player = input('enter your choice (rock, paper, scissor:)')

    print("player choice = ", player)
    print("computer choice = ", computer)

    if player == computer:
        print("it's a tie!")

    elif player == 'rock' and computer == 'scissor':
        print('you win')


    elif player == 'scissor' and computer == 'paper':
        print('you win')


    elif player == 'paper' and computer == 'rock':
        print('you win')

    else:
        print('you lose!')
    
    if input ('do you want to continue(y/n)?').lower() != 'y':
        running = False
    print('thankyou for playing')


