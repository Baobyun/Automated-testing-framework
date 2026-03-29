# 负责定位符（Locators）和业务动作
from .base_page import BasePage

class BaiduPage(BasePage):
    """百度搜索页面对象"""

    # --- 1. 定位符管理（以后元素改了，只改这里,使用通用写法） ---
    SEARCH_INPUT = "input[name='wd']"
    SEARCH_BUTTON = "input[type='submit'][value='百度一下']"

    # ---2. 业务动作封装 ---
    def search_keyword(self, keyword):
        self.fill_input(self.SEARCH_INPUT, keyword)
        # 确保按钮是“可操作”状态再点,增加显示等待
        self.page.wait_for_selector(self.SEARCH_BUTTON, state="visible")
        self.click_element(self.SEARCH_BUTTON)