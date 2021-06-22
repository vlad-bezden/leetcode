def number_of_sums(arr, k):
    counter = 0
    mapper = {}
    for i in arr:
        n = mapper.get(k - i, 0)
        counter += n
        mapper[i] = mapper.get(i, 0) + 1
    return counter


if __name__ == "__main__":
    inputs = [
        (([1, 2, 3, 4, 3], 6), 2),
        (([1, 5, 3, 3, 3], 6), 4),
        (([1], 1), 0),
        (([1, 2], 4), 0)
    ]

    for input, expected in inputs:
        output = number_of_sums(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
