# -*- coding: utf-8 -*-
"""
@File    : config.py
@Author  : wxvirus
@Time    : 2026/11/13 19:39
@Desc    : 
"""


class Config:
    def __init__(self):
        """
        关闭 wtf 的 csrf 保护
        """
        self.WTF_CSRF_ENABLED = False
