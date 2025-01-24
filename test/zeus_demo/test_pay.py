import unittest

from airtest.core.api import keyevent
from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_base, menu_pay, check
from utils import poco_android, air
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
        air.stop_zeus_demo()
        air.start_zeus_demo()
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        poco_android.find_click(menu_base.menu_base())
        poco_android.find_click(menu_base.login())
        poco_android.find_click(menu_pay.menu_pay())
        pass

    def test_google_pay(self):
        """谷歌支付"""
        poco_android.find_click(menu_pay.google_pay())
        air.sleep_dao(3)
        poco_android.find_type_click(menu_pay.pay_confirm())
        # poco_android.find_text_click(menu_pay.google_pay_confirm())
        # poco_android.find_click(menu_pay.google_pay_confirm_id())
        air.sleep_dao(10)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="谷歌支付")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_wx_pay(self):
        """微信支付"""
        poco_android.find_click(menu_pay.wx_pay())
        air.sleep_dao(3)
        poco_android.wx_pay_confirm()
        air.sleep_dao(3)
        seven,one,nine,five = menu_pay.wx_pay_password()
        poco_android.find_click(seven)
        poco_android.find_click(one)
        poco_android.find_click(nine)
        poco_android.find_click(five)
        poco_android.find_click(nine)
        poco_android.find_click(seven)
        air.sleep_dao(3)
        poco_android.find_text_click(menu_pay.wx_pay_back())
        air.sleep_dao(3)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="微信支付")

    # def test_ali_pay(self):
    #     """支付宝支付"""
    #     poco_android.find_click(menu_pay.ali_pay())
    #     air.sleep_dao(7)
    #     poco_android.set_text(menu_pay.ali_pay_account_input(),"17600116844@163.com")
    #     poco_android.find_text_click("下一步")
    #     air.sleep_zeus_demo(5)
    #     # poco_android.ali_pay_input_password1()
    #     keyevent("TAB")
    #     keyevent("14")
    #     keyevent("8")
    #     keyevent("16")
    #     keyevent("12")
    #     keyevent("16")
    #     keyevent("14")
    #     air.sleep_zeus_demo(5)
    #     # poco_android.find_click(menu_pay.pay_confirm())
    #     poco_android.find_text_click("确认付款")
    #     keyevent("14")
    #     keyevent("8")
    #     keyevent("16")
    #     keyevent("12")
    #     keyevent("16")
    #     keyevent("14")
    #     air.sleep_dao(7)
    #     poco_android.find_text_click("完成")
    #     air.sleep_dao(5)
    #     success = poco_android.find(check.zeus_yes())
    #     assert_true(success, msg="支付宝支付")


    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
