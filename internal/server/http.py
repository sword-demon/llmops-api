# -*- coding: utf-8 -*-
"""
@File    : http.py
@Author  : wxvirus
@Time    : 2026/11/9 20:39
@Desc    : Http 服务引擎
"""
import os
from pyexpat.errors import messages

from flask import Flask

from config import Config
from internal.router import Router
from internal.exception import CustomException
from pkg.response import json, Response, HttpCode


class Http(Flask):
    """Http 服务器引擎"""

    # *args 是不命名参数，命名参数要写在它之后
    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 将传递的配置信息导入进来
        self.config.from_object(conf)

    def _register_error_handler(self, error: Exception):
        # print("异常: ", error)
        # 1. 异常信息是不是我们的自定义查，如果是，可以提取 message 和 code 等信息
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))
        # 2. 如果不是自定义异常，有可能是程序或者数据库抛出的异常，也可以提取信息，设置为 Fail 状态码
        if self.debug or os.getenv("FLASK_ENV") == "development":
            # 如果是开发状态，直接抛出异常
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
