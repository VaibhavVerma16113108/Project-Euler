def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def smallest_num_evenly_divisible(lower, upper):
    arr = [i for i in range(lower, upper + 1)]
    lcm = lower
    for i in range(1, len(arr)):
        lcm = lcm * arr[i] // gcd(lcm, arr[i])

    return lcm


if __name__ == "__main__":
    lower, upper = 1, 100
    print(smallest_num_evenly_divisible(lower, upper))