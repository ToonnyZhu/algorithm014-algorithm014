#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 9:12 下午
# @Author  : Wentworth.Zhu
# @File    : No_242_valid-anagram.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        if s != t :
            return False
        return True