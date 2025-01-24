import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_test, check, menu_base
from utils import air, poco_android
from utils.logger import log


class PassLoginTest(unittest.TestCase):
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
        air.sleep_zeus_demo(5)
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        poco_android.find_click(menu_base.menu_base())
        air.sleep_zeus_demo(3)

    def test_pass_login(self):
        """账号密码登录passLogin"""
        poco_android.find_click(menu_base.pass_login())
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="账号密码登录passLogin")

    def test_pass_register(self):
        """账号密码注册passRegister"""
        poco_android.find_click(menu_base.pass_register())
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="账号密码注册passRegister")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")