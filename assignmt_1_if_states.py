name = 'Leon'
passw = 'L@oni1324'
chal_name = input('Enter Your First Name: ')
if chal_name.title() == name:
    print(f'Hello, {name}! The password is: {passw}')
else:
    print(f'Hello, {chal_name}! See you later.')
