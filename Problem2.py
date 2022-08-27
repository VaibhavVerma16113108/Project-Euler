def fibonacci_sum(a, b, total=0, limit=4e6):
    """
    Calculates the sum of even fibonacci numbers up to given limit.
    """
    if b > limit:
        return total

    if b % 2 == 0:
        total += b

    return fibonacci_sum(b, a + b, total, limit)


if __name__ == "__main__":
    print(fibonacci_sum(1, 2))
