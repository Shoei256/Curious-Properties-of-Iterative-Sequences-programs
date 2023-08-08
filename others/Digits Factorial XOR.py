import itertools
from math import factorial

def func(x):
    s=0
    for n in str(x):
        s^=factorial(int(n))
    return s
all=[itertools.combinations_with_replacement(list(range(1,10)), i) for i in range(1,8)]#all pattern you need to check

result=set()
for i,n in enumerate(itertools.chain(*all)):
    n="".join([str(a) for a in n])
    r=[]
    while n not in r:
        r.append(n)
        n=func(n)
    result.add(tuple(r[r.index(n):]))
    # r.append(n)
    # print(r)
print(result)
