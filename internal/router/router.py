# -*- coding: utf-8 -*-
"""
@File    : router.py
@Author  : wxvirus
@Time    : 2026/11/9 20:31
@Desc    : 路由
"""
from dataclasses import dataclass
from injector import inject
from flask import Flask, Blueprint
from internal.handler import AppHandler


@inject
@dataclass  # 自动生成对应的 __init__ 构造函数
class Router:
    """路由"""

    app_handler: AppHandler

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建一个蓝图 【一组路由的集合】
        # 蓝图名称
        # 导入的名字
        # 路由前缀
        bp = Blueprint('llmops', __name__, url_prefix='')

        # 2. 将 url 与对应的控制器方法进行绑定
        # app_handler = AppHandler()
        # 注意最后的是绑定的函数，不是函数的执行结果，所以不需要加上括号
        bp.add_url_rule('/ping', methods=['GET'], view_func=self.app_handler.ping)

        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
