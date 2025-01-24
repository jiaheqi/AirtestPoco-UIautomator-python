import unittest

from airtest.core.api import text
from airtest.core.assertions import assert_true

from page.zeus_demo import menu_init, menu_test, check, menu_base
from utils import air, poco_android, poco_ios
from utils.logger import log


class PayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")
        pass

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")
        # 启动demo并初始化
        # 关闭APP
        air.stop_dao_ios()
        # 打开APP
        air.start_dao_ios()
        poco_ios.find_click("初始化")
        poco_ios.find_click("静默登录")

    def test_apple_pay(self):
        """aapple支付"""
        air.sleep(2)
        poco_ios.find_click("支付")
        air.sleep(10)
        poco_ios.find_click("购买")
        poco_ios.find_click("SecureTextField")
        text("YEEM8wea.crey")
        poco_ios.find_click("登录")
        air.sleep(10)
        poco_ios.find_click("好")
        air.sleep(10)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios支付")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
