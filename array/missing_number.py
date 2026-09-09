def get_missing_number(nums: list[int]) -> int:
    n = len(nums)
    total_sum = n * (n + 1) // 2
    list_sum = sum(nums)

    return total_sum - list_sum


if __name__ == "__main__":
    print(get_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(get_missing_number([0, 1, 2, 3, 4, 6]))
