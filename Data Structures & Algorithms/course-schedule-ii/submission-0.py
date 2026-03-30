class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = []
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj_list[b].append(a)
            in_degree[a] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            node = q.popleft()
            visited.append(node)
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return visited if len(visited) == numCourses else []


        