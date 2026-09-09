"""
dictionary preserves the insertion order whereas the set is unordered
"""


def first_non_repeating(nums: list[int]) -> int:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in nums:
        if freq[num] == 1:
            return num

    return -1


if __name__ == "__main__":
    print(first_non_repeating([4, 5, 1, 2, 0, 4]))
    print(first_non_repeating([1, 1, 2, 2, 3, 3]))
    print(first_non_repeating([9, 8, 7, 8, 9, 6]))
