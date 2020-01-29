#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words,
 convert it to the canonical path.
@author: rezarashetnia
"""

class Solution(object):
    def simplifyPath(self,path):
        addresses = [p for p in path.split("/") if p !="." and p!=""]
        stack =[]
        for p in addresses:
            if p =="..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)