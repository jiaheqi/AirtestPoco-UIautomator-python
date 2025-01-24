import unittest

from airtest.core.api import keyevent
from airtest.core.assertions import assert_true
from page.account_system import base_dialog
from page.zeus_demo import menu_init, menu_base, third_platform, menu_third, check, account_system
from utils import air, poco_android
from utils.air import snapshot_screen
from utils.generates import generate_random_phone_number, generate_random_email_prefix
from utils.logger import log


class BindUnbindTest(unittest.TestCase):
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
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.menu_base())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.clear_user_account())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.login())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.menu_third())
        air.sleep_zeus_demo(5)

    def test_google_bind_and_unbind(self):
        """谷歌绑定/解绑"""
        poco_android.find_click(menu_third.google_bind())
        air.sleep_zeus_demo(3)
        poco_android.find_textMatches_click(".*gmail.com")
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="谷歌绑定")
        poco_android.find_click(menu_third.google_bind())
        poco_android.find_textMatches_click(".*gmail.com")
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="谷歌解绑")

    def test_facebook_bind_and_unbind(self):
        """facebook绑定/解绑"""
        poco_android.find_click(menu_third.facebook_bind())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="facebook绑定")
        poco_android.find_click(menu_third.facebook_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="facebook解绑")

    def test_twitter_bind_and_unbind(self):
        """twitter绑定/解绑"""
        poco_android.find_click(menu_third.twitter_bind())
        air.sleep_zeus_demo(5)
        poco_android.find_click(third_platform.twitter_ok_btn())
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="twitter绑定")
        poco_android.find_click(menu_third.twitter_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(5)
        poco_android.find_click(third_platform.twitter_ok_btn())
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="twitter解绑")

    def test_qq_bind_and_unbind(self):
        """qq绑定/解绑"""
        poco_android.find_click(menu_third.qq_bind())
        air.sleep_zeus_demo(3)
        poco_android.find_click(third_platform.qq_agree_btn())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="qq绑定")
        poco_android.find_click(menu_third.qq_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(3)
        poco_android.find_click(third_platform.qq_agree_btn())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="qq解绑")

    def test_wechat_bind_and_unbind(self):
        """wechat绑定/解绑"""
        poco_android.find_click(menu_third.wechat_bind())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="wechat绑定")
        poco_android.find_click(menu_third.wechat_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(5)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="wechat解绑")

    def test_sms_bind_and_unbind(self):
        """短信绑定/解绑"""
        poco_android.find_click(menu_third.sms_bind())
        poco_android.find_click(base_dialog.zeus_demo_agree_choose())
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
            assert_true(success, msg="短信绑定")
            poco_android.find_click(menu_third.sms_bind())
            text = poco_android.get_text(check.zeus_yes())
            success = True if text == "fail" else False
            assert_true(success, msg="短信解绑")

    def test_email_bind_and_unbind(self):
        """邮箱绑定/解绑"""
        poco_android.find_click(menu_third.email_bind())
        poco_android.find_click(base_dialog.zeus_demo_agree_choose())
        poco_android.find_click(account_system.register())
        poco_android.set_text(account_system.email_login(), generate_random_email_prefix())
        poco_android.set_text(account_system.password(), "123456")
        poco_android.set_text(account_system.password_(), "123456")
        poco_android.find_click(account_system.send())
        # 等待 verify框的出现
        if poco_android.android(account_system.codes()).wait():
            # 点两次TAB
            keyevent("TAB")
            keyevent("TAB")
            keyevent("TAB")

            keyevent("13")
            keyevent("13")
            keyevent("13")
            keyevent("13")
            air.sleep_zeus_demo(3)
            success = poco_android.find(check.zeus_yes())
            assert_true(success, msg="邮箱绑定")
        poco_android.find_click(menu_third.email_bind())
        text = poco_android.get_text(check.zeus_yes())
        success = True if text == "fail" else False
        assert_true(success, msg="邮箱解绑")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
