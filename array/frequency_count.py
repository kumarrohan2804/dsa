def frequency_count(nums: list[int]):
    dict_freq = {}
    for num in nums:
        if dict_freq.get(num):
            dict_freq[num] = dict_freq[num] + 1
        else:
            dict_freq[num] = 1

    print(dict_freq)


if __name__ == "__main__":
    frequency_count([1, 2, 3, 4, 2, 4, 1, 6, 7])
