from collections import deque
from typing import List

class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Create an adjacency list representation of the graph
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Initialize a queue with the starting node (1) and its frequency (1)
        q = deque([(1, 1)])

        # Initialize two arrays to keep track of the first and second minimum distances
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0  # The distance to the starting node is 0

        while q:
            # Dequeue the next node and its frequency
            x, freq = q.popleft()

            # Calculate the time it takes to reach the next node
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                # If the current time is in an odd interval, wait until the next even interval
                t = change * (t // change + 1) + time
            else:
                # Otherwise, just add the time it takes to reach the next node
                t += time

            # Iterate over the neighbors of the current node
            for y in g[x]:
                if dist1[y] == -1:
                    # If we haven't visited this node before, update its first minimum distance
                    dist1[y] = t
                    q.append((y, 1))
                elif dist2[y] == -1 and dist1[y] != t:
                    # If we've already visited this node once, update its second minimum distance
                    if y == n:
                        # If we've reached the destination node, return the second minimum time
                        return t
                    dist2[y] = t
                    q.append((y, 2))

        # If we haven't returned by now, it means there's no second minimum time
        return 0