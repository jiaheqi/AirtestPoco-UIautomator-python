import unittest

from airtest.core.api import keyevent
from airtest.core.assertions import assert_true

from page.account_system import login_view, base_dialog, sms_verify
from page.zeus_demo import menu_init, menu_base, third_platform, check, demo_login_view, account_system
from utils import air, poco_android
from utils.air import snapshot_screen
from utils.generates import generate_random_phone_number
from utils.logger import log
from utils.poco_android import choose_zeus_user


class LoginViewTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")
        pass

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")
        # 启动demo并初始化
        air.stop_zeus_demo()
        air.start_zeus_demo()
        air.sleep_zeus_demo(3)
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.menu_base())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.login_view())
        air.sleep_zeus_demo(2)
        poco_android.find_click(base_dialog.zeus_demo_agree())
        air.sleep_zeus_demo(2)

    def test_a_google_login(self):
        """谷歌登录"""
        air.sleep_zeus_demo(3)
        poco_android.find_click(demo_login_view.google_login())
        # poco_android.find_click(third_platform.google_select_account())
        poco_android.find_textMatches_click(".*gmail.com")
        air.sleep_zeus_demo(3)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(1)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="谷歌登录")

    def test_facebook_login(self):
        """facebook登录"""
        poco_android.find_click(demo_login_view.facebook_login())
        air.sleep_zeus_demo(10)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(1)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="facebook登录")

    def test_twitter_login(self):
        """twitter登录"""
        poco_android.find_click(demo_login_view.twitter_login())
        air.sleep_zeus_demo(5)
        poco_android.find_click(third_platform.twitter_ok_btn())
        air.sleep_zeus_demo(5)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(1)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="twitter登录")

    def test_qq_login(self):
        """qq登录"""
        poco_android.find_click(demo_login_view.qq_login())
        air.sleep_zeus_demo(3)
        poco_android.find_click(third_platform.qq_agree_btn())
        air.sleep_zeus_demo(5)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(1)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="qq登录")


    def test_wechat_login(self):
        """wechat登录"""
        poco_android.find_click(demo_login_view.wx_login())
        air.sleep_dao(10)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(1)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="wechat登录")
    def test_guest_login(self):
        """游客登录"""
        poco_android.find_click(demo_login_view.login_view_close())
        poco_android.find_click(menu_base.explicit_login())
        poco_android.find_click(menu_base.login_view())
        poco_android.find_click(base_dialog.zeus_demo_agree())
        poco_android.find_click(demo_login_view.guest_login())
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="游客登录")

    def test_email_login(self):
        """邮箱登录"""
        poco_android.find_click(demo_login_view.email_login())
        poco_android.set_text(account_system.email_login(), "charlotteplczy@gmail.com")
        poco_android.set_text(account_system.password(), "123456")
        poco_android.find_click(account_system.send())
        air.sleep_zeus_demo(3)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(2)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="邮箱登录")

    def test_sms_login(self):
        """短信登录"""
        poco_android.find_click(demo_login_view.sms_login())
        poco_android.set_text(account_system.sms(), generate_random_phone_number())
        poco_android.find_click(account_system.sms_send())
        # 等待 verify框的出现
        if poco_android.android(account_system.sms_codes()).wait():
            snapshot_screen("验证码弹窗弹出成功")

            keyevent("TAB")
            keyevent("TAB")
            keyevent("TAB")
            keyevent("TAB")

            keyevent("13")
            keyevent("13")
            keyevent("13")
            keyevent("13")
            air.sleep_zeus_demo(3)
            success = poco_android.find(check.zeus_yes())
            assert_true(success, msg="短信登录")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
