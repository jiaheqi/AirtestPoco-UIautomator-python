import unittest

from retrying import retry

from main import register_email_new_pre
from utils import air, poco_unity, poco_ios
from utils.zeus import log
from airtest.core.api import *


class EmailResetTest(unittest.TestCase):
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
    def test_email_reset_password(self):
        try:
            """ios邮箱密码重置"""
            poco_ios.find_click("iconemail")
            poco_ios.find_click("忘记密码")
            poco_ios.find_click("TextField")
            air.text(register_email_new_pre)
            SecureTextField0 = poco_ios.find_no_click_index("SecureTextField", 0)
            SecureTextField1 = poco_ios.find_no_click_index("SecureTextField", 1)
            SecureTextField0.click()
            text("1234")
            SecureTextField1.click()
            text("1234")
            poco_ios.find_click("确认重置")
            text("6666")
            air.sleep(2)
            success = poco_ios.find("请输入邮件验证码")
            poco_ios.find_click("close")
            assert_true(success, msg="dao-ios邮箱密码重置")
        except Exception as e:
            log(e)
            raise Exception

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        # 因为没有真正登录，所以不需要后置的清除账号操作
        # 结束时清空连接方便下次测试时初始化
        poco_unity.unity = None
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
