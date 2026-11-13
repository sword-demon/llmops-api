# -*- coding: utf-8 -*-
"""
@File    : app_schema.py
@Author  : wxvirus
@Time    : 2026/11/13 19:35
@Desc    : 
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""

    """
    1. 必填
    2. 长度最大为 2000
    """
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填的"),
        Length(max=2000, message="用户的提问最大长度是 2000")
    ])
