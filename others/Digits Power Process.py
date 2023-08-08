import itertools
dpp=lambda x:sum([int(n)**int(n) for n in str(x)])#operations for the each number.

all=[itertools.combinations_with_replacement(list(range(1,10)), i) for i in range(1,9)]#all pattern you need to check

loop0 = [1]
loop1 = [3435]
loop2 = [421845123,16780890]
loop3 = [16777500,2520413,3418]
loop8 = [809265896,808491852,437755524,1657004,873583,34381154,16780909,792488396]
loop11 = [791621579,776537851,19300779,776488094,422669176,388384265,50381743, 17604196,388337603,34424740,824599]
loop40 = [793312220,388244100,33554978,405027808,34381363,16824237,17647707,3341086,16824184,33601606,140025,3388,33554486,16830688,50424989,791621836, 405114593,387427281,35201810,16780376,18517643,17650825,17653671,1743552,830081, 33554462,53476,873607,18470986,421845378,34381644,16824695,404294403,387421546,17651084,17650799,776537847,20121452,3396,387467199]
loop97 = [1583236420,16827317,18470991,792441996,1163132183,16823961,404291050,387424134,17601586,17697199,1163955211,387473430,18424896,421022094,387421016, 17647705,2520668,16873662,17740759,389894501,808398820,454529386,404251154,7025,826673,17694102,388290951,808398568,454579162,388297455,421805001,16780606, 17740730,2470915,388247419,421799008,792442000,388244555,33564350,53244,3668,16870555,17656792,389164017,405068190,404247746,1694771,389114489,808395951,808401689,437799052,776491477,390761830,405067961,388340728,51155506,59159,774847229,406668854,33698038,421021659,387470537,19251281,404200841,16777992, 777358268,36074873,18471269,405068166,16920568,404294148,404198735,405024914, 387424389,421799034,775665066,1839961,791664879,793358849,809222388,437752177, 3297585,405027529,388250548,50338186,33604269,387514116,17650826,17697202, 389114241,404198251,404201349,387421291,405021541,6770,1693743,388290999]
all_loop = loop0 + loop1 + loop2 + loop3 + loop8 + loop11 + loop40 + loop97

count=0
for i,n in enumerate(itertools.chain(*all)):#Check if all numbers in the range goes to known loop.
    n="".join([str(a) for a in n])
    while True:
        n=dpp(n)
        if n in all_loop:
            count+=1
            break
print(i+1,count)#If count value equal to lenght of all it means all pattern want in to the known loop.