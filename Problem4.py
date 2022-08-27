def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


if __name__ == "__main__":
    # largest palindrome - brute force
    print(is_palindrome(9009), is_palindrome(9000))
    max_so_far = 0
    for i in range(999, 100, -1):
        for j in range(999, i, -1):
            if is_palindrome(i * j) and i * j > max_so_far:
                max_so_far = i * j
                break
    print(max_so_far)