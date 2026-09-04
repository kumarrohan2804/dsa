# Calculate the LCM of two numbers  = (num1 X num2)/GCD


def get_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def get_lcm(a: int, b: int) -> int:
    gcd = get_gcd(a, b)
    return (a * b) // gcd


if __name__ == "__main__":
    print(get_lcm(18, 12))
    print(get_lcm(14, 24))
