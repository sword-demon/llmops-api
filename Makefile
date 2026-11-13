# 用于更新 requirements.txt，命令来自 README.md
PYTHON ?= python
PIPREQ ?= pipreqs

.DEFAULT_GOAL := help

.PHONY: help deps-pipreqs deps-generate

help: ## 显示可用命令
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-16s %s\n", $$1, $$2}'

deps-pipreqs: ## 安装生成依赖文件用的 pipreqs
	$(PYTHON) -m pip install --no-deps pipreqs
	$(PYTHON) -m pip install yarg==0.1.9 docopt==0.6.2

deps-generate: deps-pipreqs ## 依据源码重新生成 requirements.txt
	$(PIPREQ) --ignore venv --force

