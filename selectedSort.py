#!/usr/bin/env python
# -*-coding:utf-8 -*-

import random
import time
source = [random.randrange(10000+i) for i in range(10000)]
def selected_sort(myList):
    # get the list
    length = len(myList)
    for i in range(0, length - 1):
        # set the smallest value of default index as now
        smallest = i
        # use now value compare with next value and get the smallest value set as index
        for j in range(i + 1, length):
            if myList[j] < myList[smallest]:
                tmp = myList[j]
                myList[j] = myList[smallest]
                myList[smallest] = tmp
    return myList
a = time.time()
print(selected_sort)
b = time.time()
print(b-a)
