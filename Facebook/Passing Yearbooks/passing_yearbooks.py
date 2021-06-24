def findSignatureCounts_naive(arr):
    result = [1] * len(arr)

    for i, v in enumerate(arr):
        while i != v - 1:
            result[i] += 1
            v = arr[v - 1]

    return result


def findSignatureCounts(arr):
    result = [None] * len(arr)
    # set of visited students
    visited = set()
    for i, v in enumerate(arr):
        # adjust index to 0 based
        v -= 1
        if i not in visited:
            # the students of the same group as student i
            group = {i}
            # keep passing the yearbook until it goes back to i
            while v != i:
                group.add(v)
                v = arr[v] - 1
            # update the visited set, with all students in the group
            visited.update(group)
            # number of times this group had signature
            signatures = len(group)
            # update each member of the group with number of signatures
            for k in group:
                result[k] = signatures
    return result


if __name__ == "__main__":
    inputs = [
        ([2, 1], [2, 2]),
        ([1, 2], [1, 1]),
        ([4, 3, 2, 1], [2, 2, 2, 2]),
        ([4, 2, 3, 1], [2, 1, 1, 2]),
        ([3, 1, 4, 2], [4, 4, 4, 4]),
        ([5, 4, 2, 3, 1], [2, 3, 3, 3, 2]),
    ]

    for input, expected in inputs:
        result = findSignatureCounts(input)
        assert result == expected, f"{input=}, {expected=}, {result=}"

    print("PASSED!!!")
