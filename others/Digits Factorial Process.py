import itertools
import math
dfp=lambda x:sum([math.factorial(int(n))for n in str(x)])#operations for the each number.

all=[itertools.combinations_with_replacement(list(range(1,10)), i) for i in range(1,7)]#all pattern you need to check

loop1A=[1]
loop1B=[2]
loop1C=[145]
loop1D=[40585]
loop2A=[871,45361]
loop2B=[872,45362]
loop3=[169,363601,1454]
all_loop=loop1A+loop1B+loop1C+loop1D+loop2A+loop2B+loop3

count=0
for i,n in enumerate(itertools.chain(*all)):#Check if all numbers in the range goes to known loop.
    n="".join([str(a) for a in n])
    while True:
        n=dfp(n)
        if n in all_loop:
            count+=1
            break
print(i+1,count)#If count value equal to lenght of all it means all pattern want in to the known loop.