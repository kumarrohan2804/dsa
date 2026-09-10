def find_duplicate(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i - 1] == nums[i]:
            return nums[i]
    return -1


if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))
    print(find_duplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))

"""
Time Complexity -----> O(nlogn)
Time Complexity -----> O(n) -- (floyd cycle detection algorithm)
"""
