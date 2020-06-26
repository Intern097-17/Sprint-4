#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Simple Calculator
def calculate(): # The calculate function
    operation = input('''
Please type in the math operation you would like to complete: # Indicates what Mathematics symbol we gonna use
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input('Please enter the first number: '))
    number_2 = float(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':                                 # In this Sprint i make use of an elif statement which allows me to check for multiple expression
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again() # Essentially Python utilises this function to repeat stuff

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for No
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you soon.')       # Essentially this is the exit function
    else:
        again()

calculate()


# In[ ]:




