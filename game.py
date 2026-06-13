import random


def play():
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} guesses.")
            break


if __name__ == "__main__":
    play()
