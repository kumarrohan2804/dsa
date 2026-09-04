def get_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(get_gcd(8, 12))
    print(get_gcd(15, 18))
