# The solution is quite similar to the max depth, but one condition we should take care is the skewed tree, skewed tree is the tree which only have node on the one side and null at the other, now we have to get the min path from root to the leaf node, we can't consider the empty nodes like skewed nodes, in that case do a simple skewed tree check, if we find any skew tree, then return max of left and right +1, +1 is because we have to consider the current node as well


# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        minLeft = self.minDepth(root.left)
        minRight = self.minDepth(root.right)

        if minLeft!=0 and minRight !=0:
            return 1 + min(minLeft,minRight)
        if minLeft == 0 :
            return 1 + minRight
        if minRight == 0:
            return 1 + minLeft
       
       