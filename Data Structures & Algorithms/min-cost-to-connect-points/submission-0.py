class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        adj_list = defaultdict(list)
        # Get distance between each point
        for i in range(num_points):
            x1, y1 = points[i]
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))
        
        total = 0
        visited = set()
        heap = [[0, 0]]

        while len(visited) < num_points:
            dist, point = heapq.heappop(heap)
            if point in visited:
                continue
            total += dist
            visited.add(point)
            for neiCost, neighbor in adj_list[point]:
                if neighbor not in visited:
                    heapq.heappush(heap, [neiCost, neighbor])

        return total
