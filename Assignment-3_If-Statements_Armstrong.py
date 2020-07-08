number = input('Enter a positive number to check if it’s an Armstrong one: ')
number_list = list(number) # For using with i iterator.
number_set = set(number) # For checking if the input is valid or not.
digit_set = set('0123456789') # For checking if the input is valid or not.
checker = 0
if number_set & digit_set == number_set:
    for i in number_list:
        checker += int(i) ** len(number)
    if checker == int(number):
        print(f'{number} is an Armstrong number')
    else:
        print(f'{number} is not an Armstrong number')
else:
    print('It is an invalid entry. Do not use non-numeric, float or negative values!')
