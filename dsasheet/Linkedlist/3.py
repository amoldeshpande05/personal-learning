# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            first = head
            second= first.next
            while first and second:
                    if first == second:
                        return True
                    first=first.next
                    second = second.next.next
        except:
            return False

        