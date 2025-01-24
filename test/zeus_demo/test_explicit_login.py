import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.account_system import base_dialog
from page.zeus_demo import menu_init, menu_base, demo_login_view, check, third_platform
from utils import air, poco_android
from utils.logger import log


class ExplicitLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")
        pass

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")

    def test_a_explicit_login_no_local_cache(self):
        """
        显示登录：本地无账号
        """
        air.stop_zeus_demo()
        air.clear_zeus_demo()
        air.start_zeus_demo()
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        poco_android.find_click(menu_base.menu_base())
        poco_android.find_click(menu_base.explicit_login())
        poco_android.find_click(base_dialog.zeus_demo_agree())
        poco_android.find_click(demo_login_view.guest_login())
        air.sleep_dao(2)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="显示登录-本地无账号")
    def test_explicit_login_local_cache(self):
        """
        显示登录：本地有账号
        """
        poco_android.find_click(menu_base.explicit_login())
        air.sleep_dao(2)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="显示登录-本地有账号")

    def test_switch_account(self):
        """
        切换账号
        """
        poco_android.find_click(menu_base.switch_account())
        poco_android.find_click(base_dialog.zeus_demo_agree())
        poco_android.find_click(demo_login_view.google_login())
        poco_android.find_click(third_platform.google_select_account())
        air.sleep_zeus_demo(3)
        poco_android.demo_choose_zeus_user()
        air.sleep_zeus_demo(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="切换账号")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
