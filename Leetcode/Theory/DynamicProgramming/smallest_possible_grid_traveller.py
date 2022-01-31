resultta=0
def gridTraveler(m,n):
    global resultta
    if m == 0 or n == 0:
        return False
    if m == 1 and n == 1:
        return True
    if gridTraveler(m-1,n) and gridTraveler(m,n-1):
        print(m-1,n,"      ",m,n-1)
    
print(gridTraveler(2,3))