import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to Guess the Number!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = input("Enter your guess (between 1 and 100): ")
        
        # Check if the input is a valid integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
    
