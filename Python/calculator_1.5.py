# Calc_1.2, new additions
# Upgraded from 2 to 4 numbers calculation
# Included BODMAS approach to it
print('Welcome to my self-made calculator!')
print('This is a project made solely by Crent')
print('This calculator is an improved version of Calc_1')
print('Involves 4 number calculation')
print(' CLICK + = ADD\n CLICK - = SUBTRACT\n CLICK * = MULTIPLY\n CLICK / = DIVIDE')

print('Calculation will be done in this way;')
print('Example: a + b - c * d')

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



#Next Calculator should include options for other calculations, like
#1. Calculation of Even or Odd numbers
#2. Calculation of Grade
#3. Calculation of Any other thing I can think of
#4. Calculation of Complex numbers and other mathematical functions
