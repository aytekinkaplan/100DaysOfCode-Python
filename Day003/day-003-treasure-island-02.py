import tkinter as tk
from tkinter import messagebox


class TreasureIslandGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Treasure Island")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Treasure Island.\nYour mission is to find the treasure.",
                              font=("Arial", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(self.root, text="Start", command=self.first_choice, font=("Arial", 14))
        self.button1.pack(pady=10)

    def first_choice(self):
        self.clear_widgets()
        self.label = tk.Label(self.root, text='You\'re at a cross road. Where do you want to go?', font=("Arial", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(self.root, text="Left", command=self.second_choice_left, font=("Arial", 14))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="Right", command=self.game_over, font=("Arial", 14))
        self.button2.pack(pady=10)

    def second_choice_left(self):
        self.clear_widgets()
        self.label = tk.Label(self.root,
                              text='You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.',
                              font=("Arial", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(self.root, text="Wait", command=self.third_choice_wait, font=("Arial", 14))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="Swim", command=self.game_over, font=("Arial", 14))
        self.button2.pack(pady=10)

    def third_choice_wait(self):
        self.clear_widgets()
        self.label = tk.Label(self.root,
                              text='You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow, and one blue. Which colour do you choose?',
                              font=("Arial", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(self.root, text="Red", command=self.game_over, font=("Arial", 14))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="Yellow", command=self.you_win, font=("Arial", 14))
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.root, text="Blue", command=self.game_over, font=("Arial", 14))
        self.button3.pack(pady=10)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def game_over(self):
        messagebox.showinfo("Game Over", "Game Over. Try again!")
        self.root.destroy()

    def you_win(self):
        messagebox.showinfo("Congratulations", "You found the treasure! You Win!")
        self.root.destroy()


root = tk.Tk()
game = TreasureIslandGame(root)
root.mainloop()
