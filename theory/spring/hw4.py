import random
import timeit
def InsertionSort(listToSort):
    toSort = listToSort[:]
    for i in range(1,len(toSort)):
        focus = toSort[i]
        j = i
        while focus < toSort[j-1] and j > 0:
            toSort[j] = toSort[j-1]#Shift element right
            j -= 1
        toSort[j] = focus #Insert the focus element after array has shifted right
    return toSort
def Merge(array1, array2):
    retArray = []
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            retArray.append(array1[0])
            array1 = array1[1:]
        else:
            retArray.append(array2[0])
            array2 = array2[1:]
    retArray += (array1 + array2)
    return retArray
def MergeSort(toSort):
    if len(toSort) > 1:
        return Merge(MergeSort(toSort[:len(toSort)/2]), MergeSort(toSort[len(toSort)/2:]))
    else:
        return toSort
def HybridSort(toSort):
    if len(toSort) > 30:
        return Merge(HybridSort(toSort[:len(toSort)/2]), HybridSort(toSort[len(toSort)/2:]))
    else:
        return InsertionSort(toSort)
def GenerateRandomList(n):
    retList = [0] * n
    for i in xrange(n):
        retList[i] = random.random()*10000
    return retList
setup='''
from __main__ import GenerateRandomList
from __main__ import MergeSort
from __main__ import HybridSort
from __main__ import InsertionSort
list10k = GenerateRandomList(10000)
list100k = GenerateRandomList(100000)
'''
results = []
print "Calculating MergeSort Time..."
results.append(min(timeit.repeat('B = MergeSort(list100k)', setup = setup, repeat=1, number = 1)))
print "Calculating HybridSort Time..."
results.append(min(timeit.repeat('B = HybridSort(list100k)', setup = setup, repeat=1, number = 1)))
print "Calculating InsertionSort Time..."
results.append(min(timeit.repeat('B = InsertionSort(list100k)', setup = setup, repeat=1, number = 1)))

"""
MergeSort: 36.260s
HybridSort: 31.197s
InsertionSort: 552.16s
"""
