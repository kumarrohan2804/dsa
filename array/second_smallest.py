def second_smallest(nums: list[int]) -> int:
    small = float("inf")
    second_small = float("inf")

    for num in nums:
        if num < small:
            second_small = small
            small = num
        elif num < second_small and num != small:
            second_small = num

    return int(second_small)


if __name__ == "__main__":
    print(second_smallest([2, 4, 5, 1, 3, 7]))
