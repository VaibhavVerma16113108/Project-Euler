import math


def sieve(n):
    primes = [True for i in range(n + 1)]
    primes[1] = False
    for i in range(4, n + 1, 2):
        primes[i] = False

    for i in range(3, n + 1, 2):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes


def is_prime(x):
    return primes[x]


def find_largest_prime_factor(n):
    for i in range(int(math.sqrt(n)), -1, -1):
        if n % i == 0 and is_prime(i):
            return i

    return n


if __name__ == "__main__":
    N = 600851475143
    SIEVE_LIMIT = int(math.sqrt(N))
    primes = sieve(SIEVE_LIMIT + 5)
    print(find_largest_prime_factor(N))