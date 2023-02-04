import random

print("Welcome to Rock, Paper, Scissors game!")
user_choice = int(input("What do you choose? Type '0' for rock, '1' for paper, or '2' for scissors \n"))
computer_choice = random.randint(0, 2)

choice = ['rock', 'paper', 'scissors']

if user_choice >= 3:
    print('Error: Not part of the choices.')
    quit()
elif user_choice == 0 and computer_choice == 2:
    print(f'You chose {choice[user_choice]}\nThe computer chose {choice[computer_choice]}\nYou Win!')
    quit()
elif user_choice == 1 and computer_choice == 0:
    print(f'You chose {choice[user_choice]}\nThe computer chose {choice[computer_choice]}\nYou Win!')
    quit()
elif user_choice == 2 and computer_choice == 0:
    print(f'You chose {choice[user_choice]}\nThe computer chose {choice[computer_choice]}\nYou Win!')
    quit()
elif user_choice == computer_choice:
    print(f'You chose {choice[user_choice]}\nThe computer chose {choice[computer_choice]}\nTie!')
    quit()
else:
    print(f'You chose {choice[user_choice]}\nThe computer chose {choice[computer_choice]}\nComputer Wins!')
    quit()




