# The logic is simple, do any order traversal, during the traversal, the behaviour of both the trees must be exactly the same!!


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True;
        if p == None or q == None:
            return False
    
        result = self.isSameTree(p.left,q.left)
        if not result:
            return False
        result = self.isSameTree(p.right,q.right)
        if not result:
            return False
        
        if p.val != q.val:
            return False
        else:
            return True
        


# Best and more effecient solution:

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True;
        if p == None or q == None:
            return False
        
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            if p.val != q.val:
                return False
            else:
                return True