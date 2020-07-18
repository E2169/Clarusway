# Here is the solution to the modified 'Prime Numbers' assignment.

n = int(input("Enter a number (n) to display prime numbers between 1 and 'n': "))
prime_list = []
for i in range(2, n + 1):
    
    for j in range(2, i + 1):
        
        if i % j == 0 and i != 2:
            
            break
        elif i == j + 1 and i % j != 0 or i == 2:
            
            prime_list.append(i)
print(prime_list)
