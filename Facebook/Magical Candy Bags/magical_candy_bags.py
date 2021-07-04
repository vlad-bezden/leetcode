import heapq


def max_candies(arr, k):
    arr = [i * -1 for i in arr]
    output = []
    heapq.heapify(arr)
    for _ in range(k):
        output.append(heapq.heappop(arr))
        heapq.heappush(arr, int(output[-1] / 2))
    return -1 * sum(output)


if __name__ == "__main__":
    inputs = [[[2, 1, 7, 4, 2], 3, 14], [[19, 78, 76, 72, 48, 8, 24, 74, 29], 3, 228]]

    for *input, expected in inputs:
        output = max_candies(*input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
