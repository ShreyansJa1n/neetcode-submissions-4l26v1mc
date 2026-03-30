# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def subtree_dfs(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            left = subtree_dfs(node1.left, node2.left)
            right = subtree_dfs(node1.right, node2.right)

            return left and right and node1.val == node2.val

        def dfs(node):
            if not node:
                return 0

            if node.val == subRoot.val:
                if subtree_dfs(node, subRoot):
                    return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left > 0 or right > 0:
                return 1
            return 0

        return dfs(root) > 0