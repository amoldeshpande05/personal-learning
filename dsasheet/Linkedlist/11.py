# Code is simple. same logic of interaction of two sorted list, but instead of adding, check the condition if it's equal then append both, if first is smaller then increated first or else increament 2nd


def findIntersection(head1,head2):
    result = Node(0)
    temp = result
    while head1 and head2:
        if head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            temp.next=Node(head1.data)
            temp = temp.next
            head1 = head1.next
            head2 = head2.next
    result = result.next
    return result