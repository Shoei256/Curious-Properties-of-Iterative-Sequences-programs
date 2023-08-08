#digit length
k=9

result=set()
for n in range(2**(k-1),2**k-1):
    # print(n)
    r=[]
    while n not in r:
        r.append(n)
        p=str(bin(n)).zfill(k+3).count("1")
        q=k-p
        m=sum([2**a for a in range(p-1)])
        n=m*(2**(q+1)-1)+2**(q-1)-2**p
    # print(r[r.index(n):])
    result.add(tuple(r[r.index(n):]))
print(result)
for n in result:
    print([bin(s) for s in n])