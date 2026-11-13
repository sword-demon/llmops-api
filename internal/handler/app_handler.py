# -*- coding: utf-8 -*-
"""
@File    : app_handler.py
@Author  : wxvirus
@Time    : 2026/11/9 20:30
@Desc    : 
"""
import os

from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq


class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"ping": "pong"}

    def completion(self):
        """
        聊天接口
        1. 提取从接口中获取的输入 POST JSON
        2. 构建 OpenAI 客户端，并发起请求
        3. 得到请求响应，然后将 OpenAI 的响应传递给前端
        """

        req = CompletionReq()
        if not req.validate():
            return req.errors

        # query = request.json.get('query')
        client = OpenAI(
            base_url=os.getenv('OPENAI_API_BASE'),
        )

        completion = client.chat.completions.create(
            model='gpt-6-astra',
            messages=[
                {'role': 'system', 'content': '你是 OpenAI 开发的聊天机器人，请根据用户的输入回复对应的信息'},
                {'role': 'user', 'content': req.query.data}
            ]
        )

        content = completion.choices[0].message.content

        return content
