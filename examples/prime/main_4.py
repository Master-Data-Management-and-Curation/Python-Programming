from prime import test_prime
from prime import is_prime as is_prime_number


def is_prime(string):
    return string == "prime"


if __name__ == "__main__":
    test_prime(1117)
    print(is_prime_number(1117))
    print(is_prime("prime"))
