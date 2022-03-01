# The logic is simple, add the base case which is when the root is 0, return 0. Now comes the real logic, return the max of leftTree's depth and rightTree's depth with +1 to consider the root




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        

        