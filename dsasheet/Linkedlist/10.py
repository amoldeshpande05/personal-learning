# Reverse two linked list and go on adding by mainitaing the carry
# Lookout for best solution


class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        #reverse first list
        
        prev=None
        curr1=first
        temp=first
        while temp!=None:
            curr1=temp
            temp=temp.next
            curr1.next=prev
            prev=curr1
        prev=None
        curr2=second
        temp=second
        while temp!=None:
            curr2=temp
            temp=temp.next
            curr2.next=prev
            prev=curr2
        
        
        carry=0
        headres=None
        
        while curr1 or curr2:
            val1=0
            val2=0
            result=0
            if curr1:
                val1 = curr1.data
            if curr2:
                val2 = curr2.data
            # print(val1,val2)
            if (val1 + val2 + carry) < 10:
                result = val1+val2+carry
                if carry>0:
                    carry-=1
            else:
                result = (val1 + val2 + carry)%10
                carry=1
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            if not headres:
                headres = Node(result)
            else:
                temp = Node(result)
                temp.next=headres
                headres = temp
                
        if carry > 0:
            if not headres:
                headres = Node(carry)
            else:
                temp = Node(carry)
                temp.next = headres
                headres = temp

        return headres