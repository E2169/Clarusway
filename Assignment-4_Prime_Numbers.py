number = int(input('Enter the number which you want to learn a prime number or not:  '))
for i in range(1, number):
    remainder = number % i
    if i != 1:
        if remainder == False:
            print(f"{number} is NOT a prime number")
            break
    if i == (number - 1):
        if remainder != False or number == 2:
            print(f"{number} is a prime number")
