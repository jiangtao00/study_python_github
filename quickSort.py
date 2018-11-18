import random
import time
source = [random.randrange(10000 + i) for i in range(10000)]
def quickSort(list,start,end):
    if start < end:
        i, j = start, end
        #set the database
        base = list[i]
        while i < j:
            while (i < j) and (list[j] >= base):
                j = j-1
            list[i] = list[j]
            while (i < j) and (list[j] <= base):
                i += 1
            list[j] = list[i]
        list[i] = base
        quickSort(list, start, i-1)
        quickSort(list, j+1, end)
    return list
list = [49,38,65,97,78,13,27,49]
print("quickSort:")
quickSort(list, 0, len(list) - 1)
print(list)
