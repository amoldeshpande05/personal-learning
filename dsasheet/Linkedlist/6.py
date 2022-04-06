# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head  
        prev = head
        while temp:
            flag = 0
            while temp and temp.next and temp.next.val == temp.val:
                temp=temp.next
            prev.next = temp.next
            prev=prev.next
            temp = temp.next
                
        return head 
            