# Time Complexity -----> O(n) + O(n)
def second_largest(nums: list[int]) -> int:
    max_value = float("-inf")
    for value in nums:
        max_value = max(max_value, value)

    min_value = float("-inf")
    min_index = -1
    for i in range(len(nums)):
        if min_value > max_value - nums[i]:
            min_index = i
    return nums[min_index]


# Time complexity Optimal One ----> O(n)
def second_largest_optimal(nums: list[int]) -> int:
    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return int(second_largest)


if __name__ == "__main__":
    print(second_largest([2, 3, 4, 18, 6, 14]))
    print(second_largest_optimal([10, 5, 8, 10, 3, 7]))
