# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(h)
# We follow only one path from the root to the target node using BST property.
#
# Space Complexity: O(h)
# Recursion stack stores function calls based on the height of the tree.
#
# h = height of the tree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are empty        
        if p is None and q is None:
            return True
        
        # One node is empty, other is not
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

