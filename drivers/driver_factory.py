
from playwright.sync_api import sync_playwright

class DriverFactory:

    @ staticmethod
    def get_browser(pw_instance, browser_type="chromium", headless=False):
        """

        :param pw_instance: playwright 启动实例
        :param browser_type: 浏览器类型
        :param headless: 是否隐藏界面运行（True 为不显示浏览器，False 为显示）
        :return:
        """
        if browser_type.lower() == "chromium":
            return pw_instance.chromium.launch(headless=headless)
        elif browser_type.lower() == "firefox":
            return pw_instance.firefox.launch(headless=headless)
        else:
            raise Exception(f"暂不支持的浏览器类型: {browser_type}")


# --- 调试代码 ---
if __name__ == "__main__":
    # 使用 with 语句确保运行完后自动关闭浏览器，不占内存
    with sync_playwright() as p:
        print("正在启动浏览器工厂...")
        # 1. 调用工厂，生产一个 Chromium 浏览器
        browser = DriverFactory.get_browser(p, browser_type="chromium", headless=False)

        # 2. 打开一个新页面
        page = browser.new_page()
        print("正在访问百度...")
        page.goto("https://www.baidu.com")

        # 3. 验证结果
        title = page.title()
        print(f"页面打开成功！标题是: {title}")

        # 4. 关闭浏览器
        browser.close()