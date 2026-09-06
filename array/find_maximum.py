def find_maximum(input_list):
    max_value = -90
    for value in input_list:
        max_value = max(max_value, value)
    return max_value


if __name__ == "__main__":
    print(find_maximum([1, 2, 3, 4, 5]))
