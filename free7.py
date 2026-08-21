print('This is the comparator of bigger or smaller than other number.')
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
bigger = n1 > n2
smaller = n1 < n2
if bigger:
    print(f'The first number {n1} is bigger than the second number {n2}.')
if smaller:
    print(f'The first number {n1} is smaller than the second number {n2}.')
