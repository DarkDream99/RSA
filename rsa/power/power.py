def power_by_mod(num_a: int, num_b: int, mod: int) -> int:
    if num_b == 0:
        return 1

    res = power_by_mod(num_a, num_b // 2, mod)
    res = (res * res) % mod
    if num_b % 2 != 0:
        res = (res * num_a) % mod

    return res


if __name__ == "__main__":
    print(power_by_mod(5, 2, 7))

