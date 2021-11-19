# swap-nodes-in-pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummyNode = ListNode(0,head)
    prev = dummyNode
    temp = head
    while temp and temp.next:
        thirdN = temp.next.next
        Fprev = temp.next
        temp.next.next=temp
        temp.next = thirdN
        prev.next = Fprev
        prev = temp
        temp = temp.next

    return dummyNode.next


# Without using dummy Node

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    temp = head
    while temp and temp.next:
        thirdN = temp.next.next
        Fprev = temp.next
        temp.next.next=temp
        temp.next = thirdN
        if prev:
            prev.next = Fprev
        else:
            head = Fprev
        prev = temp
        temp = temp.next
    
    return head