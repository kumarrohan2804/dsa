def checkarmstrong(n: int) -> bool:
    num = n
    temp = 0
    while num > 0:
        digit = num % 10
        temp = temp + (digit * digit * digit)
        num = num // 10

    return temp == n


if __name__ == "__main__":
    print(checkarmstrong(153))
    print(checkarmstrong(231))
