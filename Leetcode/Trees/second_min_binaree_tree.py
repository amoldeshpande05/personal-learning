# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/

# The solution is to get all the values in set and perform for loop to get the second min number.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        uniqueValues = set()
        def dfs(root):
            if root == None:
                return -1
            dfs(root.left)
            dfs(root.right)
            uniqueValues.add(root.val)
        dfs(root)
        minVal = root.val
        second = math.inf
        for i in uniqueValues:
            if minVal < i < second:
                second = i
        if second == math.inf:
            return -1
        return second
            
        
        