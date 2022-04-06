# splitList just like finding the middle node, write the logic of fast and slow pointer, now with the help of those pointers, create the circular list and submit.
# 1 note is to handle the even number of nodes where next.next is not None, and we need to have fast pointing towords the last node, so if next.next == head, then fast will be fast.next
class Solution:
    def splitList(self, head, head1, head2):
        fast = head
        slow = head
        while fast.next!=head:
            if fast.next.next == head:
                fast = fast.next
                break
            slow=slow.next
            fast=fast.next.next
        # print(slow.data,fast.data)
        fast.next=slow.next
        head2=slow.next
        slow.next=head
        head1=head
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2