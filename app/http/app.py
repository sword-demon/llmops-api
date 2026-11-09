# -*- coding: utf-8 -*-
"""
@File    : app.py
@Author  : wxvirus
@Time    : 2026/11/9 20:41
@Desc    : 
"""

from injector import Injector

from internal.router import Router
from internal.server import Http
import dotenv

# 将 env 加载到环境变量中
dotenv.load_dotenv()

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
