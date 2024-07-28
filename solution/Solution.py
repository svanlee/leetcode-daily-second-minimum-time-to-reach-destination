from typing import List
import heapq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            # Adjust node indices to 0-based indexing
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        # Initialize a priority queue with the starting node (0) and time (0)
        pq = [(0, 0)]

        # Initialize a list to keep track of seen times for each node
        seen = [[] for _ in range(n)]

        # Initialize a variable to keep track of the least time to reach the destination node
        least = None

        while pq:
            # Dequeue the next node and time
            t, u = heapq.heappop(pq)

            # If we've reached the destination node
            if u == n-1:
                # If this is the first time we've reached the destination node, update the least time
                if least is None:
                    least = t
                # If this is the second time we've reached the destination node, return the time
                elif least < t:
                    return t

            # If the current time is in an odd interval, wait until the next even interval
            if (t // change) & 1:
                t = (t // change + 1) * change

            # Increment the time by the travel time
            t += time

            # Iterate over the neighbors of the current node
            for v in graph[u]:
                # If we haven't seen this time before for this node, or if we've only seen one time before and it's different from the current time
                if not seen[v] or len(seen[v]) == 1 and seen[v][0] != t:
                    # Add the current time to the list of seen times for this node
                    seen[v].append(t)
                    # Enqueue the next node and time
                    heapq.heappush(pq, (t, v))