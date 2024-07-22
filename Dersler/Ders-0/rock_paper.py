import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

def main():
    root = tk.Tk()
    root.title("NOVA Rock, Paper Game")
    
    # Set window size and position
    window_width = 350
    window_height = 60
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position =  400 #(screen_width - window_width) // 2  # Center the window horizontally
    y_position = 50 #(screen_height - window_height) // 2  # Center the window vertically
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    label = tk.Label(root, text="Choose your move:")
    label.pack()

    choices = ['rock', 'paper', 'scissors']
    for choice in choices:
        button = tk.Button(root, text=choice.capitalize(), command=lambda choice=choice: play_game(choice))
        button.pack(side="left", padx=25)

    root.mainloop()

if __name__ == "__main__":
    main()
