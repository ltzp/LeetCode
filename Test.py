#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 0008 18:22
# @Author  : Letao
# @Site    : 
# @File    : Test.py
# @Software: PyCharm
# @desc    :

import re

s = re.compile(r'Created file with ([0-9]+)/([0-9]+)blocks')
line = 'Created file with 123/456blocks'
m = s.match(line)
print(m.group(0))