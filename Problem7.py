def sieve(MAXN):
    primes = {i: True for i in range(MAXN + 5)}
    primes[0] = primes[1] = False

    for i in range(4, MAXN + 5, 2):
        primes[i] = False

    for i in range(3, MAXN + 5, 2):
        if primes[i]:
            for j in range(i * i, MAXN + 5, i):
                primes[j] = False

    return primes


if __name__ == "__main__":
    MAXN = 1000000
    primes = sieve(MAXN)
    primes = list(filter(lambda x: primes[x] == True, primes))
    print(len(primes), primes[10000])