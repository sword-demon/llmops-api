# -*- coding: utf-8 -*-
"""
@File    : http.py
@Author  : wxvirus
@Time    : 2026/11/9 20:39
@Desc    : Http 服务引擎
"""

from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """Http 服务器引擎"""

    # *args 是不命名参数，命名参数要写在它之后
    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)

        # 将传递的配置信息导入进来
        self.config.from_object(conf)
