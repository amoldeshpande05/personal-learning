# Same logic as that of detect the loop

def isCircular(head):
    # Code here
    fast=head.next
    slow=head
    while fast and slow and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0
    