import heapq


def get_total_time(arr):
    output = 0
    heap = [-i for i in arr]
    heapq.heapify(heap)
    while len(heap) > 1:
        penalty = -heapq.heappop(heap) - heapq.heappop(heap)
        output += penalty
        heapq.heappush(heap, -penalty)
    return output


if __name__ == "__main__":
    inputs = [
        [[4, 2, 1, 3], 26],
        [[2, 3, 9, 8, 4], 88],
    ]

    for input, expected in inputs:
        output = get_total_time(input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
