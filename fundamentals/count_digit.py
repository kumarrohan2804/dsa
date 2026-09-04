def count_digit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)


if __name__ == "__main__":
    count_digit(1834)
