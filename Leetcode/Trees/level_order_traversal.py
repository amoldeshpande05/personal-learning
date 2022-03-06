
# The approach is same as that of bfs, but the only thing is to indicate that the level is over, we add the null, so logic will be around if curr_node is null which means the level is over, do our logic of adding and deleting and that's it, we get the answer


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        queue = [root,None]
        result=[]
        temp=[]
        while len(queue)>0:
            curr_node=queue.pop(0)            
            if curr_node == None: 
                if len(temp)>0:
                    result.append(temp)
                    temp=[]
                if len(queue) == 0:
                    break
                queue.append(None)
                continue
                
            temp.append(curr_node.val)
            if curr_node.left != None:
                queue.append(curr_node.left)
            if curr_node.right != None:
                queue.append(curr_node.right)
                
        return result
    
    
# Time Complexity : O(n)
# Space Complexity: O(3n)