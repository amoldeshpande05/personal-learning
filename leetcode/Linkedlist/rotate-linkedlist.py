# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/rotate-list/submissions/
class Solution:
    def __init__(self):
        self.head=None
        self.count=0
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        if not head or head.next == None:
            return head
        def recurRotate(temp):
            nonlocal head,k,length
            length +=1
            if temp == None or temp.next == None:
                return temp
            recurRotate(temp.next)
            k = k % length
            if k > 0:
                lastNode = temp.next
                lastNode.next = head
                head = lastNode
                temp.next = None
                k -= 1
        recurRotate(head)

        
            
        
        return head