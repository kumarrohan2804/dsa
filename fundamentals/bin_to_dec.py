import math


def convert_to_decimal(n: str) -> int:
    reverse = "".join(list(n)[::-1])
    dec = 0
    for i in range(len(reverse)):
        if reverse[i] != "0":
            dec = dec + math.pow(2, i)

    return int(dec)


if __name__ == "__main__":
    print(convert_to_decimal("1110"))
