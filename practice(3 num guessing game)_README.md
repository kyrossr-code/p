import random

play_again = True

while play_again:
    #to generate a random number betweeen 1 and 100
    secret_number = random.randint(1, 100)
    max_guesses = 10
    attempts = 0

    print("I have a number between 1 and 100. Can you guess my number?")

    # Loop until the user guesses correctly
    while attempts < max_guesses:
        guess = int(input(f"Guess a number (Attempts left: {max_guesses - attempts}): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts}!")
            break
    else:
        print(f"Game over! The number was {secret_number}.")
        
    # Ask the user if they want to play again
    response = input("\nDo you want to play again? (yes/no): ").lower()
    if response != "yes" and response != "y":
        play_again = False
        print("Thanks for playing!")
