import random

def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
