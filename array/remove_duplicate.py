def remove_duplicate(nums: list[int]):
    unique_set = set(nums)  # Order is not preserved in this

    # for num in nums:
    #     unique_set.add(num)
    print(*unique_set)


if __name__ == "__main__":
    remove_duplicate([1, 2, 3, 4, 5, 44, 4, 3, 10])
