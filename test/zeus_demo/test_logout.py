import unittest

from airtest.core.assertions import assert_true

from page.zeus_demo import menu_init, menu_test, check, menu_base
from utils import air, poco_android
from utils.logger import log


class LogoutTest(unittest.TestCase):
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
        poco_android.find_click(menu_base.login())

    def test_logout(self):
        """账号登出"""
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.logout())
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="登出")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
