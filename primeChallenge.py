from math import sqrt

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

print(isPrime(7919))
print(isPrime(1000000))
print(isPrime(6689))
print(isPrime(5813))
print(isPrime(5862))