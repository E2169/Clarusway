#  Here is the solution to the FizzBuzz assignment.

for i in range(1, 101):
    Fizz = i % 3 == 0
    Buzz = i % 5 == 0
    if Fizz and not Buzz:
        print('Fizz')
    elif Buzz and not Fizz:
        print('Buzz')
    elif Fizz or Buzz:
        print('FizzBuzz')
    else: print(i)
