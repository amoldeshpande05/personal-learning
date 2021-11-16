# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Simple soln is that, calculate the length of 2 nodes, and |l1 - l2|, whatever the difference we get, move that many number to the right on the longest list, then start comparing each linked list if both are same by incrementing one.
#  The above approach is good, only issue is that, to calculate the length, 2 extra loops/traversals are used, to avoid that, write a single loop, if any one node ends faster, assign it to head of another linked list, by doing this, we are internally doing |A - B|. At the 2nd loop, both will intersect at the same point. Return that interesection point

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1 = headA
        temp2 = headB
        while temp1 != temp2:
            if temp1 == None:
                temp1 = headB
            else:
                print("temp1. : ",temp1.val)
                temp1 = temp1.next
            if temp2 == None:
                temp2 = headA
            else:
                temp2 = temp2.next
                print("temp2. : ",temp2.val)
        return temp1
            
            
            
            