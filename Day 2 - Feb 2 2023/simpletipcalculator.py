print('Welcome to the Simple Tip Calculator!')

total_bill = float(input('What was the total bill? \n'))
num_of_people = int(input('How many people to split the bill? \n'))
tip_percentage = int(input('What percentage tip would you like to give? 3%, 7%, or 10% \n'))


def calculate_per_person(total, tip, people):
    new_pay = (total + ((tip / 100) * total)) / people
    return new_pay


final_payments = round(calculate_per_person(total_bill, tip_percentage, num_of_people), 2)
print(final_payments)
