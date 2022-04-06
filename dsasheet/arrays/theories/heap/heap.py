heap = [None,50,30,40,10,5,20,30]


def insertHeap(heap,element,n):
    heap.append(60)
    i = n+1

    while i > 1:
        parent = i//2
        if heap[parent] < heap[i]:
            # swap
            temp = heap[parent]
            heap[parent] = heap[i]
            heap[i]=temp
            i = parent
        else:
            return

def deleteHeap(heap,n):
    i=1
    heap[i] = heap[n]
    heap.pop(n)
    n=n-1
    while i < n:
        left = heap[i*2]
        right = heap[2*i+1]
        large = 2*i if left > right else 2*i+1

        if heap[large] > heap[i]:
            temp = heap[large]
            heap[large] = heap[i]
            heap[i] = temp
            i = large
        else:
            return

        

    
    

# print("Initial array is  : ",heap)
# insertHeap(heap,60,7)       
# print("after array is  : ",heap)

print("Initial array is  : ",heap)

deleteHeap(heap,7)

# print("after array is  : ",heap)




