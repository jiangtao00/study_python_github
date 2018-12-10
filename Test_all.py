#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018

# from random import randint
# num1 = randint(1, 8)
# num2 = randint(1, 8)
# results = []
# for i in range(10):
#     result = num1 * num2
# results.append(result)
# print(results)
# row = 0
# while row < 9:
#     col = 1
#     row += 1
#     while col <= 9:
#         if row < col:
#             print("\n")
#         else:
#             print("{} * {} = {}".format(col, row, col*row), end="\t")
#         col += 1

# while row < 9:
#     col = 1
#     row += 1
#     while row >= col:
#         print("{} * {} = {}".format(col, row, row*col), end="\t")
#
#         col += 1
#     print('')
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数
# money2 = [100, 60, 40, 20, 10, 0]
# money1 = reversed(money2)
# ls = []
# for i in money1:
#     ls.append(i)
# money = ls[:]
# print(money)
# rat = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# li = int(input("please enter the profit:"))
# profit = 0
# for idx in range(0, 6):
#     if li > money[idx]:
#         profit = money[idx]*rat[idx] + (li - money[idx]) * rat[idx]
#         # lis = (li-money[idx]) * lr[idx]
#         # print(lis)
#         # print(profit)
#         idx += 1
# print(profit)

# if 0 <= li <= 10:
#     li *= 0.1
#     print("{0} duller".format(li))
# elif li <= 20:
#     li = 1 + (li-10) * 0.075
#     # 0.075*li + 0.25
#     print("%d" % li)
# elif li <= 40:
#     li = 1.75 + 0.05*li
#     print("%d" % li)
# elif li <= 60:
#     li = 2.75 + 0.03*li
#     print("%d" % li)
# elif li <= 100:
#     li = 3.95 + 0.015*li
#     print("%d" % li)
# elif li > 100:
#     li = 9.95 + 0.01 * li
#     print("%d" % li)

# 题目：一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？
# x + 100 = m*m
# x + 268 = n*n
# (n+m) * (n-m) = 168 so, n-m and n+m both are the even so that n and m is odd or even

# 程序分析：
# 假设该数为 x。
# 1、则：x + 100 = n2, x + 100 + 168 = m2
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
# 7、接下来将 i 的所有数字循环计算即可
# mine
# for i in range(100):
#     if i % 2 == 0:
#         for j in range(0, 100, 2):
#
#             if i*i - j*j == 168:
#                 print(i, j, j*j-100)
#                 # print(j)
#                 # print(i*i-268)
#     else:
#         for j in range(1, 99, 2):
#             if i*i - j*j == 168:
#                 print(i, j, i*i-268)

# the answer
# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i
#         if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
#             m = (i+j) / 2
#             n = (i-j) / 2
#             x = m**2 - 268
#             print(m, n, x)

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，
# 闰年且输入月份大于2时需考虑多加一天：
# year = int(input("Year:"))
# month = int(input("Month:"))
# day = int(input("Day:"))
# days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 343]
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("this year have a day")
#     if month > 2:
#         Day = days[month-1] + 1
#         print(Day+day)
# else:
#     print(days[month-1]+day)

# the answer
# gol = 0
# if 0 < month <= 12:
#     gol = days[month - 1]
# else:
#     print("data error")
# gol += day
# leap = 0
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     leap = 1
# if leap == 1 and month > 2:
#     sum += 1
# print("it is the {} day".format(sum))

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
# lst = []
# for i in range(3):
#     x = int(input("number {0}:".format(i)))
#     lst.append(x)
# print(sorted(lst))

# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# i = int(input("the fib number that you want to know:"))
# print(fib(i))

# the answer
# def fib(n):
#     a, b = 1, 1
#     for i in range(n-1):
#         a, b = b, a+b
#     return a
# print(fib(10))
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(10))
# def fib(n):
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1]
#     fibs = [1, 1]
#     for i in range(2, n):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print(fib(10))

# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。
# a = [1, 2, 3]
# b = a[:]
# print(b)

# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{0} * {1} = {2}".format(j, i, i*j), end="\t")
#     print("")

# 题目：暂停一秒输出。并格式化当前时间
# 程序分析：使用 time 模块的 sleep() 函数。
# import time
# dicts = {"name": "john", "gender": "male"}
# for k, v in dicts.items():
#     print(k, v)
#     time.sleep(1)
# print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())))

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
# fib(func) can be worked
# f1 = 1
# f2 = 1
# for i in range(1, 22):
#     print("{0}  {1}".format(f1, f2))
#     if i % 3 == 0:
#         print('')
#     f1 = f2 + f1
#     f2 = f1 + f2

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
# from math import sqrt
# count = 0
# flag = 0
# for i in range(101, 201, 2):
#     k = int(sqrt(i))+1
#     for j in range(3, k+1):
#         if i % j == 0:
#             # print("%d No" % i)
#             # count += 1
#             flag = 1
#             break
#     if flag == 0:
#         print("Yes,{} is".format(i))
#         count += 1
#     flag = 0
#         # else:
#         #     print("No, {} is not".format(i))
#         #     count += 1
#             # break
#         # j += 1
#         # print("%d" % i)
# print(count)

# the answer
# h = 0
# leap = 1
# from math import sqrt
# for m in range(101, 201):
#     k = int(sqrt(m)+1)
#     for i in range(2, k+1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print("%d" % m)
#         h += 1
#         if h % 10 == 0:
#             print("")
#     leap = 1
# print("the total is {}".format(h))

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# for i in range(101, 1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     m = a**3 + b**3 + c**3
#     if m == i:
#         print(m)

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

# 我的思维,先找出所有质数,然后用列表存储其值,之后用所要求的结果来除以该列表中的值.
# 想复杂的原因, 循环除是从小到大,因此如果该数为合数,那么,它会被更小的质数直接分解
# from math import sqrt
# flag = 1
# l = []
# for i in range(2, 1000):
#     j = int(sqrt(i) + 1)
#     for k in range(2, j):
#         if i % k == 0:
#             flag = 0
#             break
#     if flag == 1:
#         l.append(i)
#     flag = 1
#
# k = []
# def prime(n):
#     for i in range(2, 100):
#         if n % i == 0:
#             n /= i
#             k.append(i)
#             for m in k:
#                 lk = len(k)
#                 if len(k) <
#                     print("{} * ".format(m))
#                 else:
#                     print(k)
#
#             错误,没有考虑到最后两个数都是质数
#             if n not in l:
#                 print("{}".format(i), end='*')
#             else:
#                 print("{}".format(i), end='')
#             return prime(n)
# enter = int(input("Enter a number:"))
# enter = 90
# print("result: {} = ".format(enter), end='')
# prime(enter)
# k1 = k.pop()
# for i in k:
#     print("{} * ".format(i), end='')
# print('{}'.format(k1))

#
# import time
# # 格式化成2018-11-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 打印出如下图案（菱形)
# NUM = 10
# def func(NUM):
#     # for i in range(1, NUM+1):
#     #     print(" " * (NUM+1-i))
#     for i in range(1, NUM+1, 2):
#         k = int(i / 2)
#         m = int(NUM/2 - k)
#         # print(" " * k, end="*" * i)
#         print(" " * m, end="*" * i)
#         print("")
#
#     for j in range(0, NUM+2, 2):
#         k = int(j/2)
#         m = int((NUM/2)-k)
#         print(" " * k, end="*" * (NUM-j+1))
#         print("")
# func(NUM)


# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。
# i = 0
# n = 19
# l = []
# a, b = 1, 1
# while i <= n:
#     a, b = b, a+b
#     c = b / a
#     l.append(c)
#     i += 1
# print(l)
# print(sum(l))

# the answer
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 21):
#     s += a / b
#     a, b = a+b, a
# print(s)

# 题目：求1+2!+3!+...+20!的和。
# m = 1
# s = 0
# for i in range(1, 21):
#     m *= i
#     s += m
# print(s)


# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# l = []
# char = str(input("enter 5 str:"))
# l.append(char)
# print(l)
# l=[111]
# def out(n):
#     if n == 0:
#         return None
#     else:
#         print(l.pop())
#         return out(n-1)
# print(out(1))

# def out(s, l):
#     if l == 0:
#         return
#     print(s[l-1])
#     return out(s, l-1)
# s = input("5:")
# l = len(s)
#
# out(s, l)


# 题目：有5个人坐在一起，第五个人比第4个人大2岁。第4个人比第3个人大2岁。第三个人比第2人大两岁。第2个人比第一个人大两岁。第一个人10岁。请问第五个人多大？
# 程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。
# n = 4
# x = 10
# print("last one {}".format(10))
# def old(n):
#     if n == 0:
#         return
#     else:
#         global x
#         x += 2
#         print(x)
#         return old(n-1)
# old(4)

# Answer
# def age(n):
#     if n == 1:
#         c = 10
#     else:
#         c = age(n-1) + 2
#     return c
# print(age(5))

# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# num = int(input("number:"))
# a = num // 10000
# b = num // 1000 % 10
# c = num // 100 % 10
# d = num // 10 % 10
# e = num % 10
# if a >= 1:
#     print("5")
#     s = e * 10000 + d * 1000 + c * 100 + b * 10 + a
#     print(s)
# elif b >= 1:
#     print("4")
#     s = e * 1000 + d * 100 + c * 10 + b
# elif c >= 1:
#     print("3")
#     s = e * 100 + d * 10 + c
# elif d >= 1:
#     print("2")
#     s = e * 10 + d
# else:
#     print("1")
#     print(e)

# answer
# num = list(input('输入一个最多5位的数字:'))
# print(len(num))
# num.reverse()
# for i in range(len(num)):
#     print(num[i], end='')


# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
# import re
# def judge(first, list):
#     li = []
#     first = first.upper()
#     for a in list:
#         if re.match(first, a):
#             li.append(a)
#     if len(li) == 1:
#         print(li[0])
#     else:
#         second = input('请输入第二个字母：')
#         for b in li:
#             if re.match(first + second, b):
#                 print(b)
# list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# first = input('请输入第一个字母：')
# judge(first, list)


# 题目：按相反的顺序输出列表的值。
# a = ['one', 'two', 'three']
# b = a[::-1]
# for i in b:
#     print(i)


# 题目：按逗号分隔列表。
# l = [1, 2, 3, 4, 5]
# a = ','.join(str(n) for n in l)
# print(a)


# 练习函数调用
# def hello():
#     print("hello")
# def three_hello():
#     for i in range(3):
#         print("hello")
# if __name__ == '__main__':
#     three_hello()


# 文本颜色设置
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     END = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print(bcolors.WARNING + "警告的颜色字体?" + bcolors.END)


# 求100以内的素数
# 这里使用了numpy 模块
# import numpy as np
# num = np.arange(101)
# for i in num[2:101]:
#     c = 0
#     mod = []
#     mod.append(np.mod(i, num[1:101]))
#     c = np.count_nonzero(mod)
#     if np.size(mod)-c <= 2:
#         print(i)

# 这里使用了逆向思维 和 set的特性

# a = []
# for i in range(2, 101):
#     for j in range(2, 101):
#         if i * j <= 100:
#             a.append(i * j)
# b = set(a)
# c = set(range(2, 101))
# d = c - b
# print(d)


# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
# print("enter 10 number:")
# lst = []
# for i in range(10):
#     lst.append(int(input("10number:")))
# print(sorted(lst))
# sorted(lst)

# this answer is cable but isn't capable the title
# import random
# l = []
# for i in range(10):
#     n = random.randint(1, 100)
#     l.append(n)
# print(l)
# q = sorted(l)
# print(q)

# it can be used by next way
# import random
# l = []
# for i in range(10):
#     n = random.randint(1, 100)
#     l.append(n)
# print(l)
# def select_sort(n):
#     """this is the select sort, and it can be used by sorted"""
#     for i in range(len(l)):
#         min = i
#         for j in range(i, len(l)):
#             if l[j] > l[min]:
#                 min = j
#         l[i], l[min] = l[min], l[i]
#     for i in range(len(l)):
#         print(l[i])
# select_sort(l)

# when we need enter number, we can use this follows
# N = 10
# for i in range(1, N+1):
#     input("this is the number of {}st : ".format(i))

# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
# two digest tuple is the list in the arr
# import random
# N, M = 3, 3
# arr = []
# sum = 0, 0
# for i in range(M):
#     arr.append([])
#     for j in range(N):
#         arr[i].append(random.randint(1, 10))
#     for i in range(M):
#         sum += arr[i][i]
# print(arr)

# the answer used the module of numpy'np. the reshape can generate the matrix of m,n.
# import numpy as np
# a = np.random.randint(1, 100, 9).reshape(3, 3)
# print(a)
# (m, n) = np.shape(a)
# sum = 0
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             sum += a[i, j]
# print(sum)

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
import random
ls = []
arr = []
for i in range(10):
    a = random.randint(1, 100)
    ls.append(a)
print(ls)
lst = sorted(ls)
print(lst)
m = int(input("enter a number:"))
if m > lst[9]:
    lst.append(m)
else:
    for i in range(len(lst)):
        # arr.append(i)
        for j in lst:
            if j > m:
                tmp = j
                lst[i] = j
                for k in range(i+1, len(lst)+1):
                    tmp2 = lst[k]
                    lst[k] = tmp
                    tmp = tmp2
            break
print(lst)

