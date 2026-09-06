def convertBinary(n: int) -> str:
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


if __name__ == "__main__":
    print(convertBinary(12))
    print(convertBinary(8))
    print(convertBinary(14))
