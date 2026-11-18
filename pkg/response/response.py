# -*- coding: utf-8 -*-
"""
@File    : response.py
@Author  : wxvirus
@Time    : 2026/11/18
@Desc    : HTTP 接口响应格式
"""

from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from pkg.response import HttpCode


@dataclass
class Response:
    """基础 HTTP 接口相应格式"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Any = None):
    """将统一响应对象转换为 Flask JSON 响应。"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """返回成功响应。"""
    return json(Response(data=data))
