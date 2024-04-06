import random
import tkinter as tk
from tkinter import messagebox

def get_choice_symbol(choice):
    symbols = {1: '🪨', 2: '📄', 3: '✂️'}
    return symbols.get(choice, 'Invalid choice')

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'DRAW'
    elif (user_choice == 1 and comp_choice == 2) or \
         (user_choice == 2 and comp_choice == 3) or \
         (user_choice == 3 and comp_choice == 1):
        return 'Computer'
    else:
        return 'User'

def show_result(user_choice, comp_choice):
    user_choice_symbol = get_choice_symbol(user_choice)
    comp_choice_symbol = get_choice_symbol(comp_choice)
    winner = determine_winner(user_choice, comp_choice)

    result_message = tk.Toplevel(root)
    result_message.title('Result')
    result_message.configure(bg='#f0f0f0')
    result_label = tk.Label(result_message, text=f'User choice: {user_choice_symbol}\nComputer choice: {comp_choice_symbol}\nWinner: {winner}', font=('Arial', 12), bg='#f0f0f0')
    result_label.pack(padx=20, pady=10)

def play_game():
    user_choice = int(choice_var.get())
    comp_choice = random.randint(1, 3)
    show_result(user_choice, comp_choice)

root = tk.Tk()
root.title('Rock Paper Scissors')
root.configure(bg='#f0f0f0')

tk.Label(root, text='Rock Paper Scissors', font=('Arial', 18), bg='#f0f0f0').pack(pady=10)
tk.Label(root, text='Select your choice:', font=('Arial', 12), bg='#f0f0f0').pack()

choice_var = tk.StringVar()
tk.Radiobutton(root, text='🪨 Rock', variable=choice_var, value=1, font=('Arial', 12), bg='#f0f0f0').pack()
tk.Radiobutton(root, text='📄 Paper', variable=choice_var, value=2, font=('Arial', 12), bg='#f0f0f0').pack()
tk.Radiobutton(root, text='✂️Scissors', variable=choice_var, value=3, font=('Arial', 12), bg='#f0f0f0').pack()

play_button = tk.Button(root, text='Play', command=play_game, font=('Arial', 12), bg='#4caf50', fg='white', padx=20, pady=5)
play_button.pack(pady=20)

root.mainloop()
