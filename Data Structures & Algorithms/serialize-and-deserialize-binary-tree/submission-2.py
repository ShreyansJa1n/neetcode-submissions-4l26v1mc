# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            if not node:
                ans.append("#")
                return
            ans.append(str(node.val))
            left = dfs(node.left)
            right = dfs(node.right)

        dfs(root)
        return ",".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        self.q = deque(nodes)

        def dfs():
            node_val = self.q.popleft() if self.q else "#"
            if node_val == "#":
                return None

            left = dfs()
            right = dfs()

            return TreeNode(int(node_val), left, right)

        return dfs()

