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

    def fill_input(self, selector, text):
        """输入文本"""
        # 等待元素出现在界面上，最多等10s
        self.page.wait_for_selector(selector, state="visible", timeout=10000)
        self.page.fill(selector, text)

    def wait_for_load(self):
        """等待页面加载完成"""
        self.page.wait_for_load_state("networkidle")
