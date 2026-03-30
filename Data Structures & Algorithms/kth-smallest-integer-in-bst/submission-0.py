# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            if left >= 0:
                return left
            if self.count == k:
                return node.val
            self.count += 1
            right = dfs(node.right)
            if right >= 0:
                return right

            return -1

        return dfs(root)
        