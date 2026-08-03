# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Every node in the binary tree is visited exactly once during inorder traversal.

# Space Complexity (Including Output): O(N)
# The result array stores the values of all N nodes.
# The recursive call stack requires O(H) space, where H is the height of the binary tree.
# Total: O(N) + O(H) = O(N)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def inorder(node):
            if node is None:
                return

            # Visit left subtee
            inorder(node.left)

            # Visit root
            result.append(node.val)

            # Visit right subtree
            inorder(node.right)

        inorder(root)    
        
        return result