import time
import random
source = [random.randrange(10000 + i) for i in range(10000)]
def insertSort(list):
    for i in range(i, len(list)):
        tmp = list[i]
        print(range(i - 1, -1, -1))
        for j in range(i - 1, -1, -1):
            if list[j] > tmp:
                list[j + 1] = list[j]
                list[j] = tmp
            print(list)
    return list
a = time.time()
print(insertSort)
b = time.time()
print(b - a)
