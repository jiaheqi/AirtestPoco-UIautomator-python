import unittest

from airtest.core.api import keyevent
from airtest.core.assertions import assert_true

from main import register_email_new_pre
from page.account_system import base_dialog
from page.zeus_demo import menu_init, menu_base, demo_login_view, account_system, check
from utils import poco_android, air
from utils.logger import log


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
        poco_android.find_click(menu_init.menu_init())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_init.init())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.menu_base())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.login_view())
        air.sleep_zeus_demo(2)
        poco_android.find_click(base_dialog.zeus_demo_agree())
        air.sleep_zeus_demo(5)

    def test_email_register(self):
        """邮箱注册"""
        poco_android.find_click(demo_login_view.email_login())
        air.sleep_zeus_demo(5)
        if poco_android.find_click(account_system.register()) is False:
            # 断言 没找到按钮
            assert_true(False, msg="没找到 去注册 按钮")
        poco_android.set_text(account_system.email_login(), register_email_new_pre)
        poco_android.set_text(account_system.password(), "123456")
        poco_android.set_text(account_system.password_(), "123456")
        poco_android.find_click(account_system.send())
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="邮箱注册")

    def test_email_reset_password(self):
        """邮箱密码找回"""
        poco_android.find_click(demo_login_view.email_login())
        poco_android.find_click(account_system.reset_password())
        poco_android.set_text(account_system.email_login(), register_email_new_pre)
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
            poco_android.set_text(account_system.password(), "123456")
            poco_android.find_click(account_system.send())
            air.sleep_zeus_demo(3)
            poco_android.demo_choose_zeus_user()
            air.sleep_zeus_demo(2)
            success = poco_android.find(check.zeus_yes())
            assert_true(success, msg="邮箱重置密码后登录")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")