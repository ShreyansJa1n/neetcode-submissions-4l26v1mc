class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # I first build the graph
        adj_list = {}
        for i in range(len(accounts)):
            parent_email = accounts[i][1]
            if parent_email not in adj_list:
                adj_list[parent_email] = set()
            for j in range(2, len(accounts[i])):
                adj_list[parent_email].add(accounts[i][j])
                if accounts[i][j] not in adj_list:
                    adj_list[accounts[i][j]] = set()
                adj_list[accounts[i][j]].add(parent_email)

        visited = set()
        def dfs(node, emails: List[str]) -> List[str]:
            if node in visited:
                return emails
            visited.add(node)
            emails.append(node)
            for neighbor in adj_list[node]:
                dfs(neighbor, emails)
            return emails

        res = []
        for i in range(len(accounts)):
            temp = []
            if accounts[i][1] not in visited:
                temp.append(accounts[i][0])
                all_emails = dfs(accounts[i][1], [])
                temp.extend(sorted(all_emails))
                res.append(temp)

        return res