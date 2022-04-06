
# Straight forward

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 5 6 7

class Solution:
    def reverseList(self, head):
        def helper(head): 
            if head == None or head.next == None:
                return head
            result = self.helper(head.next)
            head.next.next = head
            head.next = None

            return result

        helper(head)
        return mhead





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        temp=curr 
        while curr:
            temp = curr
            curr = curr.next
            temp.next=prev
            prev=temp
        return prev