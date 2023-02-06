import random
import string

print('Welcome to PyPassword Generator!')

try:
    # code that might raise an error
    letter_length = int(input('How many letters would you like? \n'))
    number_length = int(input('How many numbers would you like? \n'))
    symbol_length = int(input('How many symbols would you like? \n'))

    alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['!', '@', '$', '%', '^', '&', '*']

    user_char_length = letter_length + symbol_length + number_length
    character_list = alphabet + number + symbol
    print(user_char_length)

    random_list = []

    for i in range(letter_length):
        random_index_letter = random.randint(0, len(alphabet))
        random_list.append(character_list[random_index_letter])

    for i in range(number_length):
        random_index_number = random.randint(52, 61)
        random_list.append(character_list[random_index_number])

    for i in range(symbol_length):
        random_index_symbol = random.randint(62, 68)
        random_list.append(character_list[random_index_symbol])

    # print(random.shuffle(random_list))

    random.shuffle(random_list)
    new_password = "".join(random_list)
    print(f"Your new password is: {new_password}")


except Exception as e:
    # code to handle the error
    print("An error occurred:", e)
