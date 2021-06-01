import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 #intialize to any number that doesnt equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you did it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you did it")
        # else:
        #     print("wrong")
