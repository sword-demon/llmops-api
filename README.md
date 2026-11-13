# llmops-api

## 更新项目依赖

安装对应的 pipreqs 库

```bash
pip install --no-deps pipreqs
pip install yarg==0.1.9 docopt==0.6.2
```

> 生成对应的依赖包文件

```bash
pipreqs --ignore venv --force
```

根据依赖重新安装

```bash
pip install -r requirements.txt
```

## 在 docker 中安装 Postgres

```bash
# 拉取镜像
docker pull postgres
# 运行对应的容器服务
docker run --name postgres-dev -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 15432:5432 -d postgres

# 查看启动的服务
docker ps
# 关闭对应的服务
docker stop postgres-dev
```

### 创建数据库

```bash
psql -U postgres -h localhost -W

# 查看有什么数据库
\l

```

```postgresql
create database llmpos;
```

## 安装 openai 的 库

```bash
pip install --upgrade openai
```

## 安装 `python-dotenv` 来获取 `.env` 文件内的环境变量

```bash
pip install python-dotenv
```

可以通过`os.getenv('OPENAI_API_BASE')` 来获取 `.env`里的变量

## 安装 Flask-WTF

```bash
pip install -U Flask-WTF
```