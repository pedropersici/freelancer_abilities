print('This is the python simple calculator.')
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
o = str(input("Enter the operation you want to perform (+, -, *, /): "))
if o == '+':
    print('The result of the addition is: {}'.format(n1 + n2))
elif o == '-':
    print('The result of the subtraction is: {}'.format(n1 - n2))
elif o == '*':
    print('The result of the multiplication is: {}'.format(n1 * n2))
elif o == '/':
    if n2 == 0:
        print('Division by zero is not allowed.')
    else:
        print('The result of the division is: {}'.format(n1 / n2))
