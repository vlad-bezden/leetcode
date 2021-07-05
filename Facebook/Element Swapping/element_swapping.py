def find_min_array(arr: list[int], k: int) -> list[int]:
    # pointer/cursor in the list
    i = 0
    while k > 0 and i < len(arr):
        # current chunk from current pointer to the number of k available at this point
        view = arr[i : i + k + 1]
        # index of the smallest value in the current view
        min_index = arr.index(min(view), i)
        # if smallest value is not the current value
        if min_index > i:
            # remove smallest item from the list
            min_val = arr.pop(min_index)
            # and insert it to the begging of the view
            arr.insert(i, min_val)
            # update remaining number of swaps
            k -= min_index - i
        i += 1
    return arr


if __name__ == "__main__":
    inputs = [
        [[5, 3, 1], 2, [1, 5, 3]],
        [[8, 9, 11, 2, 1], 3, [2, 8, 9, 11, 1]],
        [[6, 9, 5, 2, 1], 3, [2, 6, 9, 5, 1]],
        [[5, 6, 1, 2, 6, 7, 8, 9], 3, [1, 5, 2, 6, 6, 7, 8, 9]],
        [[8, 9, 11, 2, 1], 5, [1, 8, 9, 2, 11]],
        [[8, 9, 11, 2, 1], 6, [1, 8, 2, 9, 11]],
        [[5, 6, 1, 2, 6, 7, 8, 9], 100, [1, 2, 5, 6, 6, 7, 8, 9]],
        [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2, [8, 10, 9, 7, 6, 5, 4, 3, 2, 1]],
        [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        [[5, 3, 1], 0, [5, 3, 1]],
    ]

    for *input, expected in inputs:
        output = find_min_array(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
