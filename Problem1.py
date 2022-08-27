def find_sum(n, limit):
    """
    Finds the sum of all factors of n from 1 to limit.
    >>> findSum(3, 10)
    >>> 18
    """
    first, last = n, limit // n * n - int(limit % n == 0) * n
    num_terms = (last - first) // n + 1
    return num_terms * (first + last) // 2


if __name__ == "__main__":
    limit = 1000
    answer = find_sum(3, limit) + find_sum(5, limit) - find_sum(15, limit)
    print(answer)