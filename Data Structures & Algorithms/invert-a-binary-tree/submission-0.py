# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solve(node):
            if not node:
                return None

            left = solve(node.left)
            right = solve(node.right)

            node.left, node.right = node.right, node.left

            return node

        return solve(root)