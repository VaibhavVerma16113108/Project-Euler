def sieve(MAXN):
    primes = {i: True for i in range(MAXN + 1)}
    primes[0] = primes[1] = False

    for i in range(4, MAXN + 1, 2):
        primes[i] = False

    for i in range(3, MAXN + 1, 2):
        if primes[i]:
            for j in range(i * i, MAXN + 1, i):
                primes[j] = False

    return list(filter(lambda x: primes[x] == True, primes))


def find_num_divisors(num):
    prod = 1
    for prime in primes:
        if num % prime == 0:
            count = 0
            while num % prime == 0:
                num = num // prime
                count += 1
            prod *= count + 1
    if num > 1:
        prod *= 2
    return prod


def find_triangular_number(limit):
    max_so_far, n = 0, 1
    while max_so_far < limit:
        triangular_number = n * (n + 1) // 2
        num_divisors = find_num_divisors(triangular_number)
        if num_divisors > limit:
            return triangular_number
        max_so_far = max(max_so_far, num_divisors)
        n += 1
    return 0


if __name__ == "__main__":
    MAXN = 100
    primes = sieve(MAXN)
    print(find_triangular_number(500))