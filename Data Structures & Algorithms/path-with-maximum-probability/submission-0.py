class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]

            graph[u].append((v, -succProb[i]))
            graph[v].append((u, -succProb[i]))

        heap = [(-1.0, start_node)]
        visited = {}

        while heap:
            cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited[u] = cost
            if u == end_node:
                return -cost
            
            for neighbor, prob in graph[u]:
                if neighbor not in visited:
                    heapq.heappush(heap, (-(cost * prob), neighbor))

        return 0.0

            

