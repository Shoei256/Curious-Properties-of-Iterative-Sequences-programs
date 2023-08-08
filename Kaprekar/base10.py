import itertools
import time
start=time.time()
#digit length (ex:1234->4)
k=5

#the p-th largest number
p=2

#the q-th samallest number
q=2

s=int("1"*k)
result=set()
for n in range(10**(k-1),10**k-1):
    if n%s==0:
        continue
    # print("n:",n)
    r=[]
    while n!=0:
        n=[int(a) for a in str(n).zfill(k)]
        m=sorted(set(itertools.permutations(n,k)))
        # print("m:",m)
        n=sum([m[-p][-a-1]*10**a for a in range(k)])-sum([m[q-1][-a-1]*10**a for a in range(k)])
        if n in r:
            # print(r[r.index(n):])
            result.add(tuple(r[r.index(n):]))
            break
        r.append(n)
print(result)
print(time.time()-start)
