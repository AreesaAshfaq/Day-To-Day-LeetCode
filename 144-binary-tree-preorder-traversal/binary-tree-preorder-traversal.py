# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Every node in the binary tree is visited exactly once.

# Space Complexity (Including Output):O(N)
# The result array stores the values of all N nodes.
# Recursive call stack requires O(H) space, where H is the height of the tree.
# Total: O(N) + O(H) = O(N)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        def preorder(node):
            if node is None:
                return

            result.append(node.val)

            #visit left subtree
            preorder(node.left)

            #visit right subtree
            preorder(node.right)

        preorder(root)
        return result 
        