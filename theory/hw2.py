import random
import timeit
import math

print "Average case:"
print "N -- TIME -- T(n)/n -- T(n)/nlogn -- T(n)/n^2"

for i in range(6):
    time = 0
    for j in range(20):
         time = timeit.timeit("sorted([randint(0,9) for j in range({})])".format(10**i), setup = "from random import randint", number=1000)
    time = time/20
    print "10^"+str(i)+":", time, time/(10**i), time/(((10**i)*math.log10(10**i))+1), time/(10**i)**2
    


print "Best Case:"
print "N -- TIME -- T(n)/n -- T(n)/nlogn -- T(n)/n^2"
for i in range(6):
    time = timeit.timeit("sorted([5 for i in range({0})])".format(10**(i+1)), number=1000)
    print "10^"+str(i)+":", time, time/(10**i), time/(((10**i)*math.log10(10**i)+1)), time/(10**i)**2

    

print "Worst Case:"
print "N -- TIME -- T(n)/n -- T(n)/nlogn -- T(n)/n^2"
for i in range(5):
    time = timeit.timeit("sorted([({0}) - j for j in range({0})])".format(10**(i+1)), number=1000)
    print "10^"+str(i)+":", time, time/(10**i), time/(((10**i)*math.log10(10**i))+1), time/(10**i)**2
