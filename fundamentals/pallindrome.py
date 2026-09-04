def check_pallindrome(n: int):
    num = n
    reverse_num = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        reverse_num = reverse_num * 10 + rem

    print(n == reverse_num)


if __name__ == "__main__":
    check_pallindrome(1345)
    check_pallindrome(1223221)
