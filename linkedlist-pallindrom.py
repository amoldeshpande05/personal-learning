# Definition for singly-linked list.
# https://leetcode.com/problems/palindrome-linked-list/submissions/
# The logic is simple, find out the middle point, to find the middle point, take two pointers, one increment with two points named fast and other with one point named slow/mid until fast reaches null. Once we find the middle point, reverse all the elements from the mid point to the end. Once the reverse is done, another loop from begining or head and rev, keep on compairing all the values. if both are equal then it's pallindrome, if it comes out of loop then it's not


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        mid = head
        # curr = head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
       
        right = self.reverseList(mid)
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
          
    def reverseList(self,Node):
        prev = None
        while Node:
            temp = Node.next
            Node.next = prev
            prev = Node
            Node = temp
        return prev