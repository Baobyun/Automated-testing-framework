import pytest
from pages.baidu_page import BaiduPage
from utils.yaml_utils import YamlUtil

# 调用工具读取数据
# 返回的是：{'search_keywords': ['ChatGPT 4', ...]}
raw_data = YamlUtil.read_yaml("data/baidu_data.yaml")
test_data = [str(k).strip() for k in raw_data["search_keywords"]]

# 使用装饰器：
# "keyword" 是给变量名，必须和下面函数的参数名一致
# search_keywords 是数据来源
@pytest.mark.parametrize("keyword", test_data)

def test_baidu_search_logic(page, keyword):
    # with sync_playwright() as p:
        # 暂时手动启动，conftest.py已经Fixture了
        # browser = p.chromium.launch(headless=False)
        # page = browser.new_page()
        """

        :param page:来自 conftest.py 的浏览器对象
        :param keyword：来自装饰器自动注入的搜索词
        :return:
        """

        baidu = BaiduPage(page)
        baidu.navigate("https://www.baidu.com") # 执行业务逻辑
        # page.screenshot(path="debug_baidu.png") # 看看页面到底加载出来没

        # 增加一个强制等待，确保输入框真的准备好了
        # page.wait_for_selector(BaiduPage.SEARCH_INPUT, state="attached")
        baidu.search_keyword(keyword)
        # 如果改了选择器还是不点，通常是因为焦点丢失。百度这种高度动态的页面，有时候需要你“敲一下回车”来触发
        page.keyboard.press("Enter")

        # 验证
        page.wait_for_timeout(2000) # 等 1 秒
        assert keyword in page.title()
