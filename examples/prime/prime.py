#!/usr/bin/env python
# the line before (called shbang) is optional

# imports
from math import sqrt


# function definition
def is_prime(n):
    largest_possible_divisor = int(sqrt(n)) + 1
    if n <= 1:
        return False

    for i in range(2, largest_possible_divisor):
        if n % i == 0:
            return False

    return True


# other function definition
def print_prime(n, prime):
    print(f"The number {n}", "is" if prime else "is not", "prime.")


# yet another function
def test_prime(n):
    print_prime(n, is_prime(n))


# this block only runs if it is not a library
if __name__ == "__main__":
    # local constant
    MAX = 10

    for n in range(1, MAX + 1):
        test_prime(n)
