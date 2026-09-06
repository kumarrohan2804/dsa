def reverse_array(nums: list[int]) -> list[int]:
    start = 0
    end = len(nums) - 1

    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start = start + 1
        end = end - 1

    return nums


if __name__ == "__main__":
    print(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
