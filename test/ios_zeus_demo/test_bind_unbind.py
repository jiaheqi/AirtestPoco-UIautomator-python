import unittest

from airtest.core.assertions import assert_true
from utils import air, poco_ios
from utils.logger import log


class BindUnbindTest(unittest.TestCase):
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

    # def test_apple_bind_and_unbind(self):
    #     """apple绑定/解绑"""
    #     poco_ios.find_no_click("静默登录").swipe([0, -10.0])
    #     poco_ios.find_no_click("上传角色").swipe([0, -0.1])
    #     poco_ios.find_click("新游客登录")
    #     poco_ios.find_click("Bind AppleID")
    #     poco_ios.find_click("通过密码继续")
    #     poco_ios.find_click("SecureTextField")
    #     air.text("gr20041212")
    #     poco_ios.find_click("登录")
    #     success = poco_ios.find("STATUS: Success")
    #     assert_true(success, msg="ios-appleId绑定")
    #     poco_ios.find_click("Bind AppleID")
    #     poco_ios.find_click("解绑")
    #     poco_ios.find_click("通过密码继续")
    #     poco_ios.find_click("SecureTextField")
    #     air.text("gr20041212")
    #     poco_ios.find_click("登录")
    #     success = poco_ios.find("STATUS: Success")
    #     assert_true(success, msg="ios-appleId解绑")

    def test_facebook_bind_and_unbind(self):
        """facebook绑定/解绑"""
        poco_ios.find_click("Bind Facebook")
        poco_ios.find_click("继续")
        air.sleep(2)
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("以 Heqi 的身份继续")
        air.sleep(2)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-facebook绑定")
        poco_ios.find_click("Bind Facebook")
        poco_ios.find_click("解绑")
        poco_ios.find_click("继续")
        air.sleep(2)
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("以 Heqi 的身份继续")
        air.sleep(2)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-facebook解绑")

    def test_twitter_bind_and_unbind(self):
        """twitter绑定/解绑"""
        poco_ios.find_click("Bind Twitter")
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("Authorize app")
        poco_ios.find_click("打开")
        air.sleep(2)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-twitter绑定")
        poco_ios.find_click("Bind Twitter")
        poco_ios.find_click("解绑")
        poco_ios.find_click("打开")
        air.sleep(2)
        poco_ios.find_click("Authorize app")
        poco_ios.find_click("打开")
        air.sleep(2)
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-twitter解绑")


    def test_sms_bind_and_unbind(self):
        """短信绑定/解绑"""
        poco_ios.find_click("短信绑定")
        poco_ios.find_click("selectno")
        poco_ios.find_click("TextField")
        air.text("17600116844")
        poco_ios.find_click("发送")
        air.text("6666")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-短信绑定")
        poco_ios.find_click("短信绑定")
        success = poco_ios.find("短信登录不支持解绑")
        assert_true(success, msg="ios-短信解绑")

    def test_email_bind_and_unbind(self):
        """邮箱绑定/解绑"""
        poco_ios.find_click("邮箱绑定")
        poco_ios.find_click("selectno")
        poco_ios.find_click("TextField")
        air.text("jiaheqi@topjoy.com")
        poco_ios.find_click("SecureTextField")
        air.text("1234")
        poco_ios.find_click("绑定")
        success = poco_ios.find("STATUS: Success")
        assert_true(success, msg="ios-email绑定")
        poco_ios.find_click("邮箱绑定")
        success = poco_ios.find("邮箱登录不支持解绑")
        assert_true(success, msg="ios-邮箱解绑")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
