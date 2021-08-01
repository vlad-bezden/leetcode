"""1168. Optimize Water Distribution in a Village

    https://leetcode.com/problems/optimize-water-distribution-in-a-village/
"""
import heapq


class Solution:
    @staticmethod
    def minCostToSupplyWater(n: int, wells: list[int], pipes: list[list[int]]) -> int:
        """Return the minimum total cost to supply water to all houses.

        n - number of houses
        wells - cost of building well directly in the house
        pipes - the cost to lay pipes between houses [house1, house2, cost]
        """
        # bidirectional graph represented in adjacency list
        graph = {}

        # add virtual vertex indexed with 0.
        #   then add an edge to each of the house weighted by the cost
        # Note: cost has to be before index in order for heapq to property
        #   find min value. Comparing by cost and not by house index
        graph[0] = [(cost, i) for i, cost in enumerate(wells, start=1)]

        # add the bidirectional edges to the graph
        for house_1, house_2, cost in pipes:
            graph.setdefault(house_1, []).append((cost, house_2))
            graph.setdefault(house_2, []).append((cost, house_1))

        # a set to maintain all the vertex that has been added to
        #   the final MST (Minimum Spanning Tree),
        #   starting from the vertex 0
        mst_set = set([0])

        # heap to maintain the order of edges to be visited,
        #   starting from the edges originted from vertex 0.
        # Note: we can start arbitrarily from any node
        heapq.heapify(graph[0])
        edges_heap = graph[0]
        total_cost = 0

        while len(mst_set) <= n:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                # adding the new vertex into the set to process
                mst_set.add(next_house)
                total_cost += cost
                # expanding the candidates of edge to choose from in the next round
                for cost, neighbor_house in graph.setdefault(next_house, ()):
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (cost, neighbor_house))
        return total_cost


if __name__ == "__main__":
    inputs = [
        ({"n": 3, "wells": [1, 2, 2], "pipes": [(1, 2, 1), (2, 3, 1)]}, 3),
        (
            {
                "n": 5,
                "wells": (46012, 72474, 64965, 751, 33304),
                "pipes": ((2, 1, 6719), (3, 2, 75312), (5, 3, 44918)),
            },
            131_704,
        ),
    ]

    for input, expected in inputs:
        output = Solution.minCostToSupplyWater(**input)
        assert output == expected, f"{input=}, {output=}, {expected=}"

    print("PASSED!!!")
