# 5 4 1 4 3 5 1 2
num = [5 ,4 ,1 ,4 , 3 ,5 ,1 ,2]
xxory = 0
# 1st step,find  the xor
for i in num:
    xxory ^=i

rightMostSetBit = xxory & ~(xxory-1)

x=0
y=0
for i in num:
    if (i & rightMostSetBit) == 0:
        x ^= i
    else:
        y^=i
print(x,y)

        
        

# print(bit2)

