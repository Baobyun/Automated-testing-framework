# Playwright-Pytest-POM-Framework

这是一个基于Python + Playwright + Pytest搭建的 UI 自动化测试框架，采用了工业级的 POM (Page Object Model) 设计模式。

## 技术栈
- 核心框架: Pytest
- 驱动引擎: Playwright (Chromium)
- 设计模式: Page Object Model (POM)
- 数据驱动: YAML + Pytest Parametrize
- 测试报告: Allure Report

## 项目结构说明
- `pages/`: 页面对象层，封装页面操作逻辑
- `test/`: 测试用例层
- `data/`: 存放外部测试数据 (YAML)
- `utils/`: 存放工具类 (如 YAML 读取工具)
- `conftest.py`: 全局配置与 Fixture 封装

## 如何运行
1. 安装依赖: `pip install -r requirements.txt`
2. 执行测试: `$env:PYTHONPATH="."; pytest --alluredir=report/raw`
3. 查看报告: `allure serve report/raw`