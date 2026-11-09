# -*- coding: utf-8 -*-
"""
@File    : test.py
@Author  : wxvirus
@Time    : 2026/11/9 20:24
@Desc    : 依赖注入框架 injector 测试案例
"""
from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A 的 name:{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
