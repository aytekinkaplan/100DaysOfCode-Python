import random

def display_choice(choice):
    if choice == "rock":
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif choice == "paper":
        print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
    elif choice == "scissors":
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(choices)

print("You chose:")
display_choice(user_choice)

print("Computer chose:")
display_choice(computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
