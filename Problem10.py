def sieve(MAXN):
    primes = {i: True for i in range(MAXN + 1)}
    primes[0] = primes[1] = False

    for i in range(4, MAXN + 1, 2):
        primes[i] = False

    for i in range(3, MAXN + 1, 2):
        if primes[i]:
            for j in range(i * i, MAXN + 1, i):
                primes[j] = False

    return primes


if __name__ == "__main__":
    MAXN = 2000000
    primes = sieve(MAXN)
    primes = list(filter(lambda x: primes[x] == True, primes))
    print(sum(primes))