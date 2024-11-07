import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

# Function to get computer's choice
def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

# Function to play a round
def play_round(player_choice):
    global wins, losses, ties
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    if result == "player":
        wins += 1
        result_text.set(f"You chose {player_choice}, computer chose {computer_choice}.\nYou win this round!")
    elif result == "computer":
        losses += 1
        result_text.set(f"You chose {player_choice}, computer chose {computer_choice}.\nComputer wins this round.")
    else:
        ties += 1
        result_text.set(f"You chose {player_choice}, computer chose {computer_choice}.\nIt's a tie!")
    
    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():
    score_text.set(f"Wins: {wins} | Losses: {losses} | Ties: {ties}")

    # Plot the score using Matplotlib
    labels = ['Player Wins', 'Computer Wins', 'Ties']
    scores = [wins, losses, ties]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    plt.bar(labels, scores, color=colors)
    plt.title("Rock-Paper-Scissors Scoreboard")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.ylim(0, max(scores) + 1)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

# Initialize the game variables
wins, losses, ties = 0, 0, 0

# Set up the tkinter window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Result and score text variables
result_text = tk.StringVar()
result_text.set("Make your choice to start playing.")
score_text = tk.StringVar()
score_text.set("Wins: 0 | Losses: 0 | Ties: 0")

# Create widgets
label_result = tk.Label(root, textvariable=result_text, font=("Helvetica", 14))
label_score = tk.Label(root, textvariable=score_text, font=("Helvetica", 12))
button_rock = tk.Button(root, text="Rock", command=lambda: play_round("rock"), width=10)
button_paper = tk.Button(root, text="Paper", command=lambda: play_round("paper"), width=10)
button_scissors = tk.Button(root, text="Scissors", command=lambda: play_round("scissors"), width=10)
button_quit = tk.Button(root, text="Quit", command=root.destroy, width=10)

# Place widgets on the window
label_result.pack(pady=10)
button_rock.pack(side="left", padx=10, pady=10)
button_paper.pack(side="left", padx=10, pady=10)
button_scissors.pack(side="left", padx=10, pady=10)
label_score.pack(pady=10)
button_quit.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
