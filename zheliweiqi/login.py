import unittest
from playwright.sync_api import Playwright, sync_playwright, expect


class MyTestCase(unittest.TestCase):
    def test_login_and_navigate(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("http://smarthse.51vip.biz:19902//login/supervise")
            page.get_by_role("textbox", name="请输入账号").click()
            page.get_by_role("textbox", name="请输入账号").fill("试点企业0001")
            page.get_by_role("textbox", name="请输入密码").click()
            page.get_by_role("textbox", name="请输入密码").fill("Zyj@13579")
            page.get_by_role("textbox", name="请输入验证码").click()
            page.get_by_role("textbox", name="请输入验证码").fill("supercode")
            page.get_by_role("button", name="下一步").click()
            page.locator("#workTipsclose i").click()
            with page.expect_popup() as page1_info:
                page.get_by_role("link", name="进入系统").click()
            page1 = page1_info.value
            page1.get_by_role("link", name="负责人培训证书管理列表").click()

            context.close()
            browser.close()


if __name__ == '__main__':
    unittest.main()
