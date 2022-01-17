value = 13
count=0

while value > 0:
    if value & 1 == 1:
        count+=1
    value=value>>1

print(count)
        
    
#  time complexity : (logn)

# There is a concept called n & (n-1), it will take as many operations is equal to total number of 1's

value = 13
count = 0
while value > 0:
    count+=1
    value = value & (value-1)
print(count)