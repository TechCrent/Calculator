print('Welcome to my self-made calculator!')
print('This is a calculator made solely by Crent')
print('This calculator is a simple function and has only 4 operators')
print('This calculator involves only 2 numbers')
print(' CLICK + = ADD\n CLICK - = SUBTRACT\n CLICK * = MULTIPLY\n CLICK / = DIVIDE')

print('Calculate your number')
num1 = int(input('Input your first number: '))
num2 = int(input('Input your second number: '))
opr = input("Input your operator: ")

add = '+'
sub = '-'
div = '/'
mult = '*'

if opr == add:
    print(f'Your Answer Is: {num1+num2}')
elif opr == sub:
    print(f'Your Answer Is: {num1-num2}')
elif opr == div:
    print(f'Your Answer Is: {num1/num2}')
elif opr == mult:
    print(f'Your Answer Is: {num1*num2}')
else:
    print('You have chosen the wrong operator.')



