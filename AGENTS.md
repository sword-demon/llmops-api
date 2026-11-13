# Repository Guidelines

## 项目结构与模块组织

llmops-api 是一个基于 Flask + `injector` 依赖注入的 Python 服务。

- `app/http/app.py`：服务入口，创建 `Injector` 与 `Http` 应用实例
- `internal/`：业务分层代码
    - `handler/`：控制器（`AppHandler`），处理请求
    - `router/`：路由注册，`Router` 通过 `@inject` + `@dataclass` 注入 handler
    - `server/`：`Http` 服务引擎（继承 `Flask`）
    - `core/` `middleware/` `exception/` `model/` `schema/` `service/` `task/` `schedule/` `migration/` `extension/`
      ：按职责预留的分层包
- `config/`、`pkg/`：配置与扩展代码；`storage/`：本地文件存储目录
- `test/`：测试与 HTTP 用例（`*.http`）；`docs/dev/`：开发笔记与命名规范

每个包目录必须有 `__init__.py`，并在其中用 `__all__` 收口导出（见 `internal/handler/__init__.py`）。

## 构建、测试与开发命令

```bash
pip install -r requirements.txt          # 安装 Flask、injector
pip install openai python-dotenv         # README 中说明的额外依赖，尚未写入 requirements.txt
python -m app.http.app                   # 从仓库根启动（debug 模式，端口 5000）
pipreqs --ignore venv --force            # 重新生成 requirements.txt
docker run --name postgres-dev -e POSTGRES_USER=postgres -p 15432:5432 -d postgres
```

必须从仓库根运行，否则 `internal` 等顶层包无法导入。

## 编码风格与命名约定

- 每个源文件以固定头部注释开头：

  ```python
  # -*- coding: utf-8 -*-
  """
  @File    : app_handler.py
  @Author  : wxvirus
  @Time    : 2026/11/9 20:30
  @Desc    : 应用控制器
  """
  ```

- 文件与模块名小写用下划线分隔（`app_service.py`）；类名用驼峰（`AppService`）；函数与方法用小写下划线（`generate_token`
  ）；常量全大写（`MAX_SIZE`）；私有成员前缀 `_`
- 4 空格缩进，注释与 docstring 使用中文，风格与 `docs/dev/dev.md` 保持一致

## 测试规范

仓库目前没有自动化测试框架（`pytest` 未安装）。`test/test.py` 是依赖注入的手工示例；接口用 `test/*.http`（REST
Client）验证。新增测试统一命名为 `test/test_*.py`，装好 pytest 后用 `pytest test/` 运行。

## 提交与 PR 规范

沿用 Conventional Commits，类型前缀为英文小写，描述用中文：`feat: 添加 OpenAI 聊天补全接口`、`docs: 补充项目模块用途说明`、
`chore: init llmops-api project skeleton`。分支使用 `wxvirus_codex/<简短描述>`。PR 需说明变更接口、请求示例（`.http` 或
curl）及环境变量影响。

## 安全与配置

`.env` 已被 `.gitignore` 排除，务必只提交 `.env.example`；`OPENAI_API_KEY`、`OPENAI_API_BASE` 通过 `os.getenv`
读取，禁止把真实密钥写入代码或提交记录。
