# Definition for singly-linked list.
# traverse slow variable by one pointer and fast by 2 pointers, exit when fast pointer reaches null, the slow will be the middle element


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        middle = head
        while fast and fast.next:
            fast = fast.next.next
            middle = middle.next
        return middle
        