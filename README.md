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

