class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        count = 0
        email_to_user = {}
        uf = UnionFind(len(accounts))
        for a in range(len(accounts)):
            for e in accounts[a][1:]:
                if e in email_to_user:
                    uf.union(a, email_to_user[e])
                else:
                    email_to_user[e] = a

        email_group = defaultdict(list)

        for email in email_to_user:
            user = uf.find(email_to_user[email])
            email_group[user].append(email)

        output = []
        for user in email_group:
            output.append([str(accounts[user][0])] + email_group[user])
        return output
        