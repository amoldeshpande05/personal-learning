# https://www.youtube.com/watch?v=ugQ2DVJJroc&t=311s

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev=curr
            curr=temp
        return prev
            
# consider two pointers, prev-> which is pointing to previous node and curr which is pointing to the current node. take the temp variable and go to the next node for the reference. point curr to next, temp to curr and your loop is done

    def reverseListRecurr(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None or head.next == None:
                return head
            newHead = self.reverseListRecurr(head.next)
            head.next.next = head
            head.next = None
            return newHead
        
    # This is by Recurrsion method, where we will stop until we find the new head which is the last node, and head will be pointing towords the last second node. we keep on changing the head.next.next to the head node and head to None, we go on doing like this and all the elements will be reversed.