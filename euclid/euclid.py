from typing import Tuple


def base_euclid():
    raise NotImplementedError()


def extend_euclid(num_a: int, num_b: int) -> Tuple[int, int, int]:
    """
    GCD(a, b) = m = x * a + y * b

    :param num_a: number a
    :param num_b: number b
    :return: (GCD(a, b), x, y)
    """
    if num_a == 0:
        x = 0
        y = 1
        return num_b, x, y

    gcd, x1, y1 = extend_euclid(num_b % num_a, num_a)
    x = y1 - (num_b // num_a) * x1
    y = x1
    return gcd, x, y

