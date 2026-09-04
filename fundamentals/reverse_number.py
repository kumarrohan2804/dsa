def reverse_number(n: int):
    reverse_num = 0
    while n > 0:
        rem = n % 10
        reverse_num = reverse_num * 10 + rem
        n = n // 10
    print(f"Reverse number : {reverse_num}")


if __name__ == "__main__":
    reverse_number(4765)
