# Definition for singly-linked list.

# Find out the cycle by floyd's cycle detection algorithm, once you find, store that meeting point. the algorithm also states that if we go on continuing by incrementing head and the meet pointer, We will end up at the point at which the cycle is taking place





class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow=slow.next
            fast = fast.next.next
            if slow == fast:
                while head!=fast:
                    head = head.next
                    fast = fast.next
                return head
        
        return None