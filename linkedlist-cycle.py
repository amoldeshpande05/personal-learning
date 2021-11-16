# Definition for singly-linked list.
# My approach, save the values in a list, and keep on checking in a loop, hashmap approach
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = []
        while head:
            if head in temp:
                return True
            else:
                temp.append(head)
                head = head.next
        
        return False
        

# cycle detection algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # temp = []
        # while head:
        #     if head in temp:
        #         return True
        #     else:
        #         temp.append(head)
        #         head = head.next
        
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        
        while slow and fast:
            if slow == fast:
                return True
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False
        
        
        return False