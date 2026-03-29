#  所有的页面都有共同的操作（点击、输入、等待）
# -*- coding: utf-8 -*-

class BasePage:

    def __init__(self, page):
        # 这里的 page 是 playwright 的 Page 对象
        self.page = page

    def navigate(self,url):
        """跳转页面"""
        self.page.goto(url)

    def click_element(self, selector):
        """点击元素"""
        self.page.click(selector)

    def fill_input(self, selector, text, timeout=20000): # 把等待时间从 10000 提到 20000
        # 增加一个检查：如果元素没出现，打印出来
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout)
            self.page.fill(selector, text)
        except Exception as e:
            print(f"云端找不到这个元素: {selector}")
            # 自动截图，就能在 Actions 产物里看到它到底卡在哪了
            self.page.screenshot(path="debug_error.png")
            raise e

    def wait_for_load(self):
        """等待页面加载完成"""
        self.page.wait_for_load_state("networkidle")
