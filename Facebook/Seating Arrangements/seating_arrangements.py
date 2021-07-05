def min_overall_awkwardness(arr: list[int]) -> int:
    arr.sort()
    counter = 0
    for i in range(len(arr) - 2):
        counter = max(counter, arr[i + 2] - arr[i])
    return counter


if __name__ == "__main__":
    inputs = [
        [[5, 10, 6, 8], 4],
        [[1, 2, 5, 3, 7], 4],
        [[2, 4, 6, 20, 40], 34],
        [[24, 98, 2, 54, 87, 76, 45, 2, 67, 37], 35],
    ]

    for input, expected in inputs:
        output = min_overall_awkwardness(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED")
