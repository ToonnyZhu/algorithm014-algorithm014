#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:23 下午
# @Author  : Wentworth.Zhu
# @File    : No_70_climbing-stairs.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def climbStairs(self, n: int) -> int:
        # 取巧 面向测试用例编程
        # a = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733,1134903170,1836311903]
        # return a[n-1]

        # 公式法
        import math
        sqrt_5 = 5 ** 0.5
        secular_equation = math.pow((1+sqrt_5)/2,n+1) - math.pow((1-sqrt_5)/2,n+1)
        answer = int(secular_equation/sqrt_5)
        return answer