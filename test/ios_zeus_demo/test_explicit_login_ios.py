import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.account_system import base_dialog
from page.zeus_demo import menu_init, menu_base, demo_login_view, check, third_platform
from utils import air, poco_android, poco_ios
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
        # 关闭APP
        air.stop_dao_ios()
        # 打开APP
        air.start_dao_ios()
        air.sleep(7)
        poco_ios.find_click("初始化")
        poco_ios.find_click("静默登录")

    def test_a_explicit_login_no_local_cache(self):
        """
        显示登录：本地无账号
        """
        poco_ios.find_click("注销")
        air.sleep(3)
        poco_ios.find_click("显示登录")
        poco_ios.find_click("selectno")
        poco_ios.find_click("user2")
        air.sleep(2)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios显示登录-本地无账号")

    def test_explicit_login_local_cache(self):
        """
        显示登录：本地有账号
        """
        poco_ios.find_click("显示登录")
        air.sleep(3)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios显示登录-本地有账号")

    def test_switch_account(self):
        """
        切换账号
        """
        poco_ios.find_click("switchAccount")
        poco_ios.find_click("selectno")
        poco_ios.find_click("iconemail")
        poco_ios.find_click("TextField")
        air.text("jiaheqi@topjoy.com")
        poco_ios.find_click("SecureTextField")
        air.text("1234")
        poco_ios.find_click("登录")
        poco_ios.find_click("游戏账号")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios切换账号-邮箱登录")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
