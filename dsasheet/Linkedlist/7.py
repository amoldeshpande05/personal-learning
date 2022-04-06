# Store it in dictionary and go on adding the values.l..

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head
        values = dict()
        values[head.data] = True
        previous = head
        temp=head.next
        while temp:
            if temp.data not in values:
                values[temp.data] = True
                previous.next=temp
                previous=previous.next
            temp = temp.next
        previous.next=temp
                 
        # code here
        # return head after editing list
        return head
