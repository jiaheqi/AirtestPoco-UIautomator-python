import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_base, menu_pay, check
from utils import air, poco_android
from utils.logger import log


class SubscriptionTest(unittest.TestCase):
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
        poco_android.find_click(menu_base.menu_base())
        poco_android.find_click(menu_base.login())
        poco_android.find_click(menu_pay.menu_pay())
        pass

    def test_google_subscription(self):
        """谷歌订阅"""
        poco_android.find_click(menu_pay.google_subscription())
        air.sleep_dao(12)
        poco_android.find_type_click(menu_pay.pay_confirm())
        # poco_android.find_text_click(menu_pay.google_pay_confirm())
        # poco_android.find_click(menu_pay.google_pay_confirm_id())
        air.sleep_dao(20)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="谷歌订阅")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
