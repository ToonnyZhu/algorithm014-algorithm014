#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:18 下午
# @Author  : Wentworth.Zhu
# @File    : No_20_valid-parentheses.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["?"] # 巧妙地避免了“((”这种情况，牛批
        for i in s:
            if i == "(" :
                stack.append(")")
                #print(stack)
            elif i == "{" :
                stack.append("}")
            elif i == "[" :
                stack.append("]")
            else:
                last_value = stack.pop()
                #print(i,last_value)
                if last_value != i :
                    return False
        return len(stack) ==1