def union_array(nums1: list[int], nums2: list[int]) -> list[int]:
    union_set = set(nums1 + nums2)
    print(list(union_set))
    return nums1


if __name__ == "__main__":
    union_array([1, 2, 3], [3, 4, 5])
    union_array([1, 1, 2, 2], [2, 3, 3])
    union_array([5, 10, 15], [10, 20, 25])
