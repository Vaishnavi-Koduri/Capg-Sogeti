n = int(input("Enter the 1st num: "))
m = int(input("Enter the 2nd num: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num(n, m):
    primes = []
    for num in range(n, m + 1):
        if is_prime(num):
            primes.append(num)
    return primes

primes = prime_num(n, m)
print("Prime numbers:", primes)
max_prime= max(primes)
min_prime= min(primes)
print("Maximum prime:", max_prime)
print("Minimum prime:", min_prime)