class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        visited = set()
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))
        heapq.heappush(heap, (0, k))
        time = 0
        while heap:
            time_node, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, time_node)
            for nei in adj_list[node]:
                heapq.heappush(heap, (time + nei[1], nei[0]))
        return time if len(visited)==n else -1