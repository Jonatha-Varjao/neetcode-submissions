# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        
        def posorder(node):
            if not node:
                return 
            posorder(node.left)
            posorder(node.right)
            self.result.append(node.val)
        
        posorder(root)
        return self.result