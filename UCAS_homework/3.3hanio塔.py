# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 01:20:40 2019

@author: 79877
"""
from typing import List 
##################################################
def move(n,a,b,c):   #n为圆盘数，a代表初始位圆柱，b代表过渡位圆柱，c代表目标位圆柱
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)   #将初始位的n-1个圆盘移动到过渡位，此时初始位为a，上一级函数的过渡位b即为本级的目标位，上级的目标位c为本级的过渡位
		print(a,'-->',c)
		move(n-1,b,a,c)


