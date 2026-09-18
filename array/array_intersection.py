def intersection_array(nums1: list[int], nums2: list[int]) -> list[int]:
    n1 = len(nums1)
    n2 = len(nums2)
    inter_array = []
    min_length = min(n1, n2)
    for i in range(min_length):
        if nums1[i] in nums2:
            inter_array.append(nums1[i])

    return inter_array


if __name__ == "__main__":
    print(intersection_array([1, 2, 3], [3, 4, 5]))
    print(intersection_array([1, 2, 3, 4], [3, 4, 5, 6]))
