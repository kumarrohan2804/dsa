def move_negatives(nums: list[int]) -> list[int]:
    n = len(nums)
    positive_list = []
    j = 0
    for i in range(n):
        if nums[i] <= 0:
            nums[j] = nums[i]
            j += 1
        else:
            positive_list.append(nums[i])
    k = 0
    while j < n:
        nums[j] = positive_list[k]
        k += 1
        j += 1

    return nums


if __name__ == "__main__":
    print(move_negatives([1, -2, 3, -4, 5, -6]))
    print(move_negatives([1, 2, 3, 4]))
    print(move_negatives([-5, 3, -2, 8, -1, 4]))
