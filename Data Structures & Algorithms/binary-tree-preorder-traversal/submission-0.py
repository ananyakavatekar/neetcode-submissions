# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Pre order ROOT LEFT RIGHT

        output = []

        def recurse(node):
            if (node == None):
                return
            
            output.append(node.val)
            recurse(node.left)
            recurse(node.right)
        
        recurse(root)

        return output
        