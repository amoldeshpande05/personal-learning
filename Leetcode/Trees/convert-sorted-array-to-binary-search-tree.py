# the logic is based on the binary search, write a helper function, with the basic binary search condition with if l<r, and middle will be the root, and make it calculate the left side middle element and right side middle element and keep on going down

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            if l>r:
                return None
            middle = (l+r)//2
            root = TreeNode(nums[middle])
            root.left = helper(l,middle-1)
            root.right = helper(middle+1,r)
            return root
        return helper(0,len(nums)-1)
        
                        
                        
                    
            
                
        