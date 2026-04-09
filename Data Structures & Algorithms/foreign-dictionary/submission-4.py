class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj_list}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        q = deque()
        for i in adj_list:
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj_list[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(res) if len(res) == len(adj_list) else ""