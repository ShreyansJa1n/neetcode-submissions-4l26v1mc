# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, cur_max):
            if not node:
                return
            if node.val >= cur_max and node.val >= root.val:
                self.ans += 1

            cur_max = max(cur_max, node.val)
            
            left = dfs(node.left, cur_max)
            right = dfs(node.right, cur_max)
            return

        dfs(root, root.val)
        return self.ans