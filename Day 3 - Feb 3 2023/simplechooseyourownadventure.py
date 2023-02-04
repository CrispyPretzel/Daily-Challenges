print('Welcome to Treasure Island \nYour mission is to find the treasure.')

chosen_path = input('Your at a crossroad. Which way do you choose? Type "left" or "right"\n')

if chosen_path == 'left':
    chosen_action = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                          'boat. Type "swim" to swim across\n')
elif chosen_path == 'right':
    print('You go back home.')
    quit()
else:
    print('Error: Not any of the choices')
    quit()

if chosen_action == 'swim':
    chosen_activity = input(
        'You swam for a while but finally reached the island. Type "dig" to dig for treasure. Type "leave" to go back home.\n')

elif chosen_action == 'wait':
    print('You waited but no boat came so you went back home')
    quit()

else:
    print('Error: Not any of the choices')
    quit()

if chosen_activity == 'dig':
    print('CONGRATULATIONS YOU FOUND THE TREASURE!!!')

elif chosen_activity == 'leave':
    print('After all this time trying to find the treasure you went back home')
    quit()

else:
    print('Error: Not any of the choices')
    quit()