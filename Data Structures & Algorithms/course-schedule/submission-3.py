class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for p, c in prerequisites:
            adj_list[c].append(p)
            indegree[p] += 1
        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            course = q.popleft()
            finish += 1

            for c in adj_list[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return finish == numCourses