# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Every node in the binary tree is visited exactly once during postorder traversal.

# Space Complexity (Including Output): O(N)
# The result array stores the values of all N nodes.
# The recursive call stack requires O(H) space, where H is the height of the binary tree.
# Total: O(N) + O(H) = O(N)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def postorder(node):
            if node is None:
                return
            
            # Visit left subtree
            postorder(node.left)
            
            # Visit right subtree
            postorder(node.right)

            # Visit root
            result.append(node.val)

        postorder(root)

        return result