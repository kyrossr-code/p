import random

max_rounds = 5
player_score = 0
computer_score = 0
print(f"Welcome to Rock, Paper, Scissors! Best of {max_rounds} rounds wins.")

for round_num in range(max_rounds):
    print(f"\n--- Round {round_num + 1} ---")
    
    # Get player choice
    choices = ["rock", "paper", "scissors"]
    while True:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player in choices:
            break
        print("Invalid choice! Please enter rock, paper, or scissors.")
    
    computer = random.choice(choices)

    print(f"Computer chose: {computer}")
    print(f"You chose: {player}")
    
    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
    
    print(f"Score: You {player_score} - Computer {computer_score}")

# Game over
print(f"\n=== Game Over ===")
print(f"Final Score: You {player_score} - Computer {computer_score}")
if player_score > computer_score:
    print("You win the match!")
elif computer_score > player_score:
    print("Computer wins the match!")
else:
    print("It's a tie!")
