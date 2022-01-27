import random

# choices array
choices = [
    'rock',
    'paper',
    'scissors'
]

# game state
game = True

# player and computer scores
p_score = 0
c_score = 0

# whole game options
while game:
    # computer choice
    computer_choice = random.choice(choices)
    # player choice
    player_choice = input(
        "Enter your choice (rock, paper or scissors): ").lower()

    # tie options
    if player_choice == computer_choice:
        print("it's tie!")
        print(f"Player score: {p_score}")
        print(f"Computer score: {c_score}")
    # computer win options
    elif ((player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock")):
        c_score += 1
        print(
            f"P choice {player_choice} and C choice {computer_choice}, Computer win!")
        print(f"Player score: {p_score}")
        print(f"Computer score: {c_score}")
    # player win options
    elif ((player_choice == 'rock' and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper")):
        p_score += 1
        print(
            f"P choice {player_choice} and C choice {computer_choice}, Player win!")
        print(f"Player score: {p_score}")
        print(f"Computer score: {c_score}")
    else:
        game = False
        print("Error! something went wrong...")
