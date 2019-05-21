def power_by_mod(num_a: int, num_b: int, mod: int) -> int:
    res = 1
    for i in range(0, num_b):
        res *= num_a
        res %= mod

    return res
