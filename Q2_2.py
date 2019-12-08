'''
Q2_2)Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
counter = 0
for iteration in range (0,5):
    counter += 1
    for pattern in range (0, counter-1):
        print ('*', end = ' ')
    print()
for iteration in range (0,5):
    counter -= 1
    for pattern in range (0, counter+1):
        print ('*', end = ' ')
    print()