n1 = float(input("Enter the student's first grade: "))
n2 = float(input("Enter the student's second grade"))
if n1 > 10.0:
  print('This calculation is impossible.')
elif n2 > 10.0:
  print('This calculation is impossible.')
else:
  m = (n1 + n2)/2
  if m < 6.0:
    print('The student didn't pass the grade.')
  else:
    print('The student passed the grade.')
