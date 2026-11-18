# -*- coding: utf-8 -*-
"""
@File    : __init__.py.py
@Author  : wxvirus
@Time    : 2026/11/9 20:08
@Desc    : 处理异常信息
"""

from .exception import (
    CustomException,
    FailException,
    NotFoundException,
    ForbiddenException,
    UnauthorizedException,
    ValidationError
)

__all__ = [
    "CustomException",
    "FailException",
    "NotFoundException",
    "ForbiddenException",
    "UnauthorizedException",
    "ValidationError",
]
