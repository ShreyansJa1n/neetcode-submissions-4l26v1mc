class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        stack = set()

        adj_list = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            adj_list[a].append(b)

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for n in adj_list[node]:
                if n not in visited:
                    if dfs(n):
                        return True

                elif n in stack:
                    return True

            stack.remove(node)
            return False

        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False

        return True

