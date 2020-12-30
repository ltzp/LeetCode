#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/27
# @Author  : yuetao
# @Site    : 
# @File    : 表示数值的字符串.py
# @Desc    :

"""
有限状态机算法
"""
from enum import Enum


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END",
        ])  # 中间转换的状态
        self.Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL",
        ]) #操作

        transfer = {
            State.STATE_INITIAL: {
                self.Chartype.CHAR_SPACE: State.STATE_INITIAL,
                self.Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                self.Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                self.Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
            },
            State.STATE_INT_SIGN: {
                self.Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                self.Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            },
            State.STATE_INTEGER: {
                self.Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                self.Chartype.CHAR_EXP: State.STATE_EXP,
                self.Chartype.CHAR_POINT: State.STATE_POINT,
                self.Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT: {
                self.Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                self.Chartype.CHAR_EXP: State.STATE_EXP,
                self.Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT_WITHOUT_INT: {
                self.Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            },
            State.STATE_FRACTION: {
                self.Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                self.Chartype.CHAR_EXP: State.STATE_EXP,
                self.Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_EXP: {
                self.Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                self.Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
            },
            State.STATE_EXP_SIGN: {
                self.Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            },
            State.STATE_EXP_NUMBER: {
                self.Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                self.Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_END: {
                self.Chartype.CHAR_SPACE: State.STATE_END,
            },
        } #状态的转换
        st = State.STATE_INITIAL
        for c in s:
            cur_type = self.to_char_type(c)
            if cur_type not in transfer[st]:
                return False
            st = transfer[st][cur_type]
        if st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER,
                  State.STATE_END]:
            return True
        else:
            return False

    def to_char_type(self, char):
        if char.isdigit():
            return self.Chartype.CHAR_NUMBER
        elif char.lower() == "e":
            return self.Chartype.CHAR_EXP
        elif char == ".":
            return self.Chartype.CHAR_POINT
        elif char == "+" or char == "-":
            return self.Chartype.CHAR_SIGN
        elif char == " ":
            return self.Chartype.CHAR_SPACE
        else:
            return self.Chartype.CHAR_ILLEGAL


if __name__ == '__main__':
    solve = Solution()
    s = "3.1416"
    result = solve.isNumber(s)
    print(result)
