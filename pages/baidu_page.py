# 负责定位符（Locators）和业务动作
from .base_page import BasePage

class BaiduPage(BasePage):
    """百度搜索页面对象"""

    # --- 1. 定位符管理（以后元素改了，只改这里） ---
    SEARCH_INPUT = "#kw"
    SEARCH_BUTTON = "#su"

    # ---2. 业务动作封装 ---
    def search_keyword(self,keyword):
        """搜索某个关键字的完整流程"""
        self.fill_input(self.SEARCH_INPUT, keyword)
        self.click_element(self.SEARCH_BUTTON)