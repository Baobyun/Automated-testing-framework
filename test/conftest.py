# 统一配置浏览器，因为：浏览器环境被识别出了“自动化特征”见debug_baidu图片，导致虽然元素在那，但 Playwright 无法与其交互。

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """自动化管理浏览器的生命周期 """
    with sync_playwright() as p:
        # slow_mo=500 动作减速，防止百度识别太快有效规避反爬检测
        browser = p.chromium.launch(
            headless=True,
            slow_mo=500,
            args=["--disable-blink-features=AutomationControlled"] #环境伪装 disable-blink-features 规避反爬检测
        )
        # 模拟真实的浏览器环境
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        yield page  # 将 page 借给测试用例,传参def test_baidu_search_logic(page):

        browser.close()
