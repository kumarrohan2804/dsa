def get_minimum(nums: list[int]) -> int:
    min_value = float("inf")
    for value in nums:
        min_value = min(min_value, value)
    return int(min_value)


if __name__ == "__main__":
    print(get_minimum([2, 4, 3, 1, 3, 4]))
