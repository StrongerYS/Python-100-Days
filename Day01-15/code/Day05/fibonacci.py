"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

"""
def Fibonacci(num):
    val1 = 1
    val2 = 1
    ret = []
    count = 0
    while count<num:
        ret.append(val1)
        count+=1
        tmp = val1 + val2
        val1 = val2
        val2 = tmp
    return ret

print(Fibonacci(20))
"""
