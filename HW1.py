import random

primes = []
mx = []

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i + 1):
        primes.append(i + 1)

for i in range(3):
    mx.append(random.sample(primes,3))

print(*mx, sep = "\n")