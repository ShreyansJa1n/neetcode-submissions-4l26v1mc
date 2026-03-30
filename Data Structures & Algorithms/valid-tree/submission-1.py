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
                if parent is not None and child == parent:
                    continue
                if child in visited:
                    return True
                else:
                    if dfs(child, node):
                        return True

            return False

        if dfs(0, None):
            return False

        return True if len(visited) == n else False

