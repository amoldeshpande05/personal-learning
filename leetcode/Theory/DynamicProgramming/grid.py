memo = {}
def gridTraveler(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m,n) in memo.keys():
        return memo[(m,n)]
    memo[(m,n)] = gridTraveler(m-1,n) + gridTraveler(m,n-1)
    return memo[(m,n)]




print(gridTraveler(3,3))