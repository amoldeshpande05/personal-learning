# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 
        dummy = ListNode(0,head)
        prev = dummy
        firsthalfHead = None
        temp = None
        while head:      
            while head and head.val < x:
                if  not firsthalfHead:
                    firsthalfHead = head
                    temp = firsthalfHead
                else:
                    temp.next = head
                    temp=temp.next
                head = head.next
            prev.next = head
            prev=prev.next
            if head:
                head = head.next          
        
        if firsthalfHead:
            temp.next =  dummy.next 
            return firsthalfHead
        else:
            return dummy.next
        
        
# amazing code with bigO(n) time complexity, where run the loop to eliminate the values < x and parallely make the linked list of nodes lesser than the x, at the end just join it.
                    
        
                
        