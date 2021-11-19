# Definition for singly-linked list.
# Approach is simple, take 1 variable, go on creating the alternate linked list by jumping one, take secode variable, start from 2nd node, go on jumping one node untill the last node. as soon as 1s't variable's last node's address is Null, go and end the loop. At the end stich two linkedlist together


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        temp1 = head
        head2 = head.next
        temp2 = head2
        while temp1 and temp2 and temp1.next:
            temp1.next = temp2.next
            if temp2 and temp1.next:
                temp1 = temp1.next
                temp2.next = temp1.next
                temp2 = temp2.next
        # head.next = head2
        temp1.next = head2
        return head
        
    