import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 10)

    # Set the number of attempts
    attempts = 0

    while True:
        # Ask the player to guess the number
        player_guess = input("Enter your guess: ")

        # Ensure the input is a valid number
        try:
            player_guess = int(player_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check if the player's guess is correct
        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


# Run the game
guessing_game()
