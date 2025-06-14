# Calc_2.0, new additions
# Upgraded from 2 numbers to unlimited(potentially) numbers
# Options for other calculations, like:
    #1. Calculation of Even or Odd numbers
    #2. Calculation of Grade
    #3. Calculation of Any other thing I can think of
    #4. Calculation of Complex numbers and other mathematical functions
# Add loop functions
# Add menu and home functions
# Add return functions

# Improve print statements
# Make it visually apealing
# Think of how to add color codes
# Think of how to add font sizes, styles, etc.

#This is the success code from Calc_1.3, recalibrate to match goals of Calc_2.0
print('Welcome to my Akalx, multipurpose Calculator 1.0')
print('Created by Crent')
print('Inspired from Proj. Calc_1.3')

print('CALCULATE YOUR NUMBER.')
num1 = float(input('Input your first number: '))
opr1 = input("Input your first operator: ")

num2 = float(input('Input your second number: '))
opr2 = input("Input your second operator: ")

num3 = float(input('Input your third number: '))
opr3 = input("Input your third operator: ")
num4 = float(input('Input your last number: '))

process = f'{num1} {opr1} {num2} {opr2} {num3} {opr3} {num4}'
result = eval(process)
print(f'Your Answer is: {result}')
