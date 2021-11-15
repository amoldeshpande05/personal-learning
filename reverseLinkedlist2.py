# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.dummy=None
        self.revHead=None
        self.revTemp=None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        self.dummy = ListNode(0,head)
        temp = self.dummy
        pre = temp
        post = temp
        count=0
#       Finding the pre
        while temp:
            count+=1
            if count <= left-1:
                pre = pre.next
            if count <= right:
                post = post.next
            temp = temp.next
            
        postPlus = post.next
        post.next = None
        head,tail = self.displayReverse(pre.next)
        pre.next = head
        tail.next=postPlus
        
        return self.dummy.next
                
    def displayReverse(self,pre):
        if not pre:
            return None
        else:   
            self.displayReverse(pre.next)
            if not self.revHead:
                self.revHead = pre
                self.revTemp = self.revHead
            else:
                self.revTemp.next = pre
                self.revTemp = self.revTemp.next
        return self.revHead,self.revTemp
        
        
        
        
        
        
# 
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = head
        curr = pre
        nxt = pre
        flast=pre
        count=1
        temp = None
        tump=curr
        prev=None
        while curr:
            if count == left-1:
                pre = curr
            if count == left:
                flast = curr
            if count >= left and count < right:
                if count == left:
                    temp = curr.next
                if temp:
                    nxt = temp.next
                    prev=curr.next
                    curr.next.next=curr
                    print("curr.val : ",curr.val)
                    curr=temp
                    temp=nxt
            elif count>right:
                break;
            else:
                curr=curr.next
            count+=1
            tump=tump.next
        print("pre.valuue : ",prev.val)
        print("flast.valuue : ",flast.val)
        print("curr.valuue : ",temp.val)

        pre.next = flast
        temp.next = tump
                
        return head
    
    
    
    
    # My Best solution
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        DummyNode=ListNode(0,head)
        prev=DummyNode
        curr = head
        if right-left == 0 or head.next == None:
            return head
        for i in range(1,left):
            prev = curr
            curr = curr.next
        newHead,newTail = self.reverseLinkedList(curr,right-left)
        prev.next = newHead
        curr.next = newTail
        return DummyNode.next
    def reverseLinkedList(self,curr,length): #return newHead, Tail
        prev = None

        for i in range(0,length+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev,curr