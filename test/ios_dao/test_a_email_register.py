import unittest

from retrying import retry

from main import register_email_new_pre
from page.game import homes
from utils import air, dao_util, poco_unity, poco_ios
from utils.zeus import log
from airtest.core.api import *


class EmailRegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")
        # 关闭APP
        air.stop_dao_ios()
        # 打开APP
        air.start_dao_ios()
        air.sleep(7)
        poco_ios.find_click("selectno")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_register(self):
        """ios邮箱注册"""
        try:
            poco_ios.find_click("iconemail")
            poco_ios.find_click("去注册")
            poco_ios.find_click("TextField")
            air.text(register_email_new_pre)
            air.sleep(3)
            SecureTextField0 = poco_ios.find_no_click_index("SecureTextField", 0)
            SecureTextField1 = poco_ios.find_no_click_index("SecureTextField", 1)
            SecureTextField0.click()
            text("1234")
            air.sleep(3)
            SecureTextField1.click()
            text("1234")
            poco_ios.find_click("注册")
            air.sleep(5)
            success = poco_unity.find(homes.menu_button())
            assert_true(success, msg="dao-ios邮箱注册")
        except Exception as e:
            log(e)
            raise Exception

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        air.sleep(2)
        dao_util.open_account_center()
        parent, child = homes.logout_account()
        poco_unity.find_and_click_child_element(parent, child)
        # 结束时清空连接方便下次测试时初始化
        poco_unity.unity = None
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
