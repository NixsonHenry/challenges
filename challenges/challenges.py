# Chanllenge 008
# Ask for the total price of the bill, then ask how many diners there are. Divide the total
# bill by the number of diners and show how much each person must pay. 

""" 
total_price = int(input("what is the total price of the bill?: "))
number_of_diners = int(input("How many diners are there?: "))

each_person_pay = total_price/number_of_diners

print(f'Each person must pay: {each_person_pay} $')
"""

# Chanllenge 012
# Ask for two numbers. If the first one is larger than the second, display the second number 
# first and then the first number, otherwise show the first number first and then the second. 

""" 
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print(second_number)
    print(first_number)
else:
    print(first_number)
    print(second_number)
"""

# Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, 
# display the message “Too high”, otherwise display “Thank you”
""" 
number = float(input("Enter a number less than 20: "))
if number >= 20:
    print("Too high")
else:
    print("Thank you")
"""

# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within 
# this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.
"""
number = float(input("Enter a number between 10 to 20: "))
if number >= 10 and number <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
"""







