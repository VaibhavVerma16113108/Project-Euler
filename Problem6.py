def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2


if __name__ == "__main__":
    n = 100
    print(sum_of_squares(n) - square_of_sum(n))