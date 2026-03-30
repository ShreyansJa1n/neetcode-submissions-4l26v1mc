class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for child in adj_list[node]:
                if child not in visited:
                    dfs(child, node)


        dfs(0, None)

        return len(visited) == n

