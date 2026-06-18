import random
import string

pool = string.ascii_letters + " "
goal = 'a computer science portal for geeks'

best = ''
best_score = 0


def score(s):
    return sum(1 for i in range(len(goal)) if s[i] == goal[i])

while True:
    generated = ''.join(random.choices(pool, k= len(goal)))

    current_score = score(generated)

    if current_score > best_score:
        best_score = current_score
        best = generated
        print("Best so far:", best)
        print("score:", best_score)


    if generated == goal:
        print("Found!")
        break

