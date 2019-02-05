import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1.0)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(-1, 200):
        if is_prime(i):
            print(i)
