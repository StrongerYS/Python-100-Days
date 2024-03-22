"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
# print(f"area: {area:.2f}, perimeter: {perimeter:.2f}") #使用format，括号中变量带冒号后指定输出格式
