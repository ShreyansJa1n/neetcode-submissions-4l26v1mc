# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if not node:
                return [0, 0]

            left = solve(node.left)
            right = solve(node.right)
            return [max(left[0], right[0]) + 1, max(max(left[1], right[1]), left[0] + right[0])]

        return solve(root)[1]