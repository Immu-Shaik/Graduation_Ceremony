def count_ways(n):
    if n<4:
        return str(2**(n-1))+'/'+str(2**n)
    C=2
    CC=1
    CCC=1
    P = 4
    count = 8
    for i in range(4,n+1):
        temp= CCC
        CCC=CC
        CC=C
        C=P
        P= count
        count = (count-temp)*2+temp
    return str(CCC+CC+C)+'/'+str(count)

print(count_ways(5))
print(count_ways(10))

