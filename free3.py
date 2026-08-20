print('We’re going to evaluate you to see if you can get this job.')
P1 = bool(input('Do you have a degree? (True or False): '))
P2 = bool(input('Do you have experience in this area? (True or False):  '))
if P1 and P2:
    print('You are qualified for this job.')
elif P1 or P2:
    print('You can work in this job.')
else:
    print('You are not qualified for this job.')
