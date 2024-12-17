# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0 
        
        def dfs(node):
            nonlocal count  
            if not node:  
                return 0
            
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            count += 1
            
            return l + r + 1  
        
        dfs(root)  
        return count
        