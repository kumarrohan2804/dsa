def move_zeroes(nums: list[int]) -> list[int]:
    j = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    while j < n:
        nums[j] = 0
        j += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))
    print(move_zeroes([0, 0, 1]))
    print(move_zeroes([1, 2, 3]))
    print(move_zeroes([4, 0, 5, 0, 0, 6]))
