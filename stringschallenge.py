first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip().title().rjust(22)

# Second challenge
second_value = second_value.replace('-','').strip().capitalize()

# Third challenge
third_value = third_value.strip().replace(' ', '').replace('-',' ').capitalize().rjust(32)

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print('fourth#fifth#sixth!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'{"fourth":^22}\n{"fifth":^22}\n{"sixth":^22}')