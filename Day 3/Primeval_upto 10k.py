# Print all the primes between 1 to 10000

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# # Print primes from 1 to 10,000
for num in range(1, 10001):
    if prime(num):
        print(num, end=" ")