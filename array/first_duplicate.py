def first_duplicate(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1


if __name__ == "__main__":
    print(first_duplicate([2, 1, 3, 5, 3, 2, 4]))
    print(first_duplicate([1, 2, 3, 4, 5]))
