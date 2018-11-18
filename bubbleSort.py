import random
import time
source = [random.randrange(10000 + i) for i in range(10000)]

c
def bubble_sort():

    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


a = time.time()
print(bubble_sort)
b = time.time()
print(b - a)
