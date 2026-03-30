class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            print(node)
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            return

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count