import unittest

from retrying import retry

from utils.generates import  generate_random_phone_number
from utils.logger import log
from utils import poco_unity, poco_ios, dao_util
from utils import air
from airtest.core.api import *


class SmsLoginTest(unittest.TestCase):
    """因为短信无法真正登录成功，所以单独拆分一个测试类"""
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")
        air.stop_dao_ios()
        # 打开APP
        air.start_dao_ios()
        air.sleep(10)
        poco_ios.find_click("selectno")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_sms_login(self):
        """ios短信登录"""
        try:
            poco_ios.find_click("iconmobile")
            poco_ios.find_click("TextField")
            text(generate_random_phone_number())
            poco_ios.find_click("发送")
            text("6666")
            success = poco_ios.find("请填写手机短信验证码")
            poco_ios.find_click("close")
            assert_true(success, msg="dao-ios短信登录")
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
