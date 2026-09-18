def move_even_odd(nums: list[int]) -> list[int]:
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums


if __name__ == "__main__":
    print(move_even_odd([-2, -3, -4, 5, 6]))
    print(move_even_odd([1, 2, 3, 4, 5, 6]))
    print(move_even_odd([0, 1, 2, 3, 4, 5]))
