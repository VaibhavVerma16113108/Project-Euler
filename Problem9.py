def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def find_product():
    for c in range(1, 501):
        for b in range(1, c):
            for a in range(1, b):
                if is_pythagorean_triplet(a, b, c) and a + b + c == 1000:
                    print(a, b, c)
                    return a * b * c


if __name__ == "__main__":
    print("Product:", find_product())
