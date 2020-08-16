#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:22 下午
# @Author  : Wentworth.Zhu
# @File    : No_66_plus-one.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 取巧做法
        # number = [ i *10**index for index,i in enumerate(digits[::-1])]
        # number_addup = sum(number)
        # number_addup += 1
        # final_list = list(map(int,str(number_addup)))
        # return final_list

        # newlist = []
        # while digits and digits[-1] == 9 :
        #     digits.pop()
        #     newlist.append(0)
        # if not digits :
        #     return [1] + newlist
        # else :
        #     digits[-1] += 1
        #     return digits + newlist

        for i in range(len(digits)-1, -1, -1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
                    return digits

