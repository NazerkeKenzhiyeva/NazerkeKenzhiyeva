import random

def guess():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num = random.randint(1, 20)
    tries = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        tries += 1

        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {tries} guesses!")
            break

guess()
