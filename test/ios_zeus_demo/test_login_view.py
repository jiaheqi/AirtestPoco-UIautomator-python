import unittest

from airtest.core.api import text
from airtest.core.assertions import assert_true

from utils import air, poco_ios
from utils.generates import generate_random_phone_number
from utils.logger import log


class LoginViewIosTest(unittest.TestCase):
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
        poco_ios.find_click("初始化")
        poco_ios.find_click("界面登录")
        poco_ios.find_click("selectno")

    # def test_apple_id_login(self):
    #     poco_ios.find_click("iconapple")
    #     poco_ios.find_click("通过密码继续")
    #     poco_ios.find_click("SecureTextField")
    #     air.text("gr20041212")
    #     poco_ios.find_click("登录")
    #     success = poco_ios.find("STATUS: Success")
    #     assert_true(success, msg="ios-appleid登录")

    def test_email_login(self):
        poco_ios.find_click("iconemail")
        poco_ios.find_click("TextField")
        air.text("jiaheqi@topjoy.com")
        poco_ios.find_click("SecureTextField")
        air.text("1234")
        poco_ios.find_click("登录")
        poco_ios.find_click("游戏账号")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-email登录")
    def test_facebook_login(self):
        poco_ios.find_click("iconfacebook")
        poco_ios.find_click("继续")
        air.sleep(2)
        poco_ios.find_click("打开")
        air.sleep(2)
        # poco_ios.find_textMatches_click("以.*的身份继续")
        poco_ios.find_click("以 Heqi 的身份继续")
        air.sleep(2)
        poco_ios.find_click("游戏账号")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-facebook登录")

    def test_guest_login(self):
        """ios游客登录"""
        poco_ios.find_click("user2")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-游客登录")

    def test_sms_login(self):
        poco_ios.find_click("iconmobile")
        poco_ios.find_click("TextField")
        text(generate_random_phone_number())
        # text("17600116844")
        poco_ios.find_click("发送")
        text("6666")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-短信登录")

    def test_twitter_login(self):
        poco_ios.find_click("icontwitter")
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("Authorize app")
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("游戏账号")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-twitter登录")



    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")


    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
