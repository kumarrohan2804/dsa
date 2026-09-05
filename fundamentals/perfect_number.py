import math


def is_perfect(n: int) -> bool:
    num = n
    temp_sum = 1
    range_value = math.ceil(math.sqrt(n))
    for i in range(2, range_value):
        if n % i == 0:
            temp_sum = temp_sum + i + (num // i)
    return n == temp_sum


if __name__ == "__main__":
    print(is_perfect(6))
    print(is_perfect(14))
    print(is_perfect(28))
