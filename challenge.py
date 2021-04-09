print('Would you like to continue?')
keepGoing = input()
if keepGoing == 'no' or keepGoing == 'n':
    print('Exiting')
elif keepGoing == 'yes':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no')
