import math


def prime_checker(number):
    if n <= 1:
        return print(f"It's not a prime number.")
    if n == 2:
        return print(f"It's a prime number.")
    if n % 2 == 0:
        return print(f"It's not a prime number.")
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return print(f"It's not a prime number.")
    return print(f"It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
