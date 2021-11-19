# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     [1,2,3,3,4,4,5]
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        temp = head
        blackList=set()
        allValues=set()
        lastVal=0
        while temp:
            if temp.next and temp.next.val == temp.val:
                blackList.add(temp.val)
            allValues.add(temp.val)
            lastVal = temp.val
            temp = temp.next
            
        allValues.difference(blackList)
        allValues = list(allValues)
        blackList = list(blackList)

        head = None
        temp = None
        allValues.sort()
        for i in allValues:
            if i not in blackList:
                tempNode =  ListNode(i,None)
                if not head:
                    head = tempNode
                    temp = head
                else:
                    temp.next = tempNode
                    temp = temp.next
        return head
                    
                    
# My method of storing it in a list, removing the duplicate elements and then building the new linked list, which will take O(2N) of time




# The following method, takes one dummy node and then goes on checking for the next node.
#  youtube link  : https://www.youtube.com/watch?v=R6-PnHODewY



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     [1,1,1,2,3]
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        prev = dummyNode
        while prev:
            flag = 0
            while head and head.next and head.next.val == head.val:
                head = head.next
                flag = 1
            if flag == 1:
                prev.next = head
            else:
                prev.next = head
                prev = prev.next
            if head:
                head=head.next
        return dummyNode.next
                
        
        
        
        