import unittest

from retrying import retry

from main import register_email_new_pre
from utils.generates import generate_random_phone_number
from utils.logger import log
from utils import poco_unity, poco_ios, dao_util
from utils import air
from airtest.core.api import *
from page.game import homes


class ThirdBindTest(unittest.TestCase):
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
        poco_ios.find_click("user2")
        air.sleep(10)
        dao_util.open_account_center()

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_bind(self):
        """ios邮箱绑定"""
        try:
            parent, child = homes.email_bind()
            poco_unity.find_and_click_child_element(parent, child)
            poco_ios.find_click("selectno")
            poco_ios.find_click("TextField")
            text(f"{register_email_new_pre}@gmail.com")
            # text("2024022700@gmail.com")
            poco_ios.find_click("SecureTextField")
            text("1234")
            poco_ios.find_click("绑定")
            air.sleep(2)
            fail = poco_ios.find("邮箱绑定")
            poco_ios.find_click("close")
            success = not fail
            assert_true(success, msg="dao-ios邮箱绑定")
        except Exception as e:
            log(e)
            raise e

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_sms_bind(self):
        """ios短信绑定"""
        try:
            parent, child = homes.sms_bind()
            poco_unity.find_and_click_child_element(parent, child)
            poco_ios.find_click("selectno")
            poco_ios.find_click("TextField")
            air.text(generate_random_phone_number())
            poco_ios.find_click("发送")
            air.text("6666")
            success = poco_ios.find("请填写手机短信验证码")
            poco_ios.find_click("close")
            assert_true(success, msg="dao-ios短信绑定")
        except Exception as e:
            log(e)
            raise Exception


    # def test_google_login(self):
    #     poco_android.find_click(login_view.google_login())
    #     air.sleep(3)
    #     poco_android.find_text_click("autouitopjoy@gmail.com")
    #     # 没有绑定多用户则不需要选择zeus账号
    #     air.sleep(5)
    #     poco_android.choose_zeus_user()
    #     air.sleep(5)
    #     # 判断如果找到菜单按钮，登录成功
    #     success = poco_unity.find(homes.menu_button())
    #     assert_true(success, msg="dao-谷歌登录")
    #
    # def test_facebook_login(self):
    #     poco_android.find_click(login_view.facebook_login())
    #     air.sleep(10)
    #     poco_android.find_textMatches_click(".*身份继续")
    #     air.sleep(20)
    #     poco_android.choose_zeus_user()
    #     air.sleep(5)
    #     # 判断如果找到菜单按钮，登录成功
    #     success = poco_unity.find(homes.menu_button())
    #     assert_true(success, msg="dao-facebook登录")

    # def test_twitter_login(self):
    #     """dao-twitter登录"""
    #     poco_android.find_click(login_view.twitter_login())
    #     air.sleep(5)
    #     poco_android.find_click(third_platform.twitter_ok_btn())
    #     air.sleep(10)
    #     success = poco_unity.find(homes.menu_button())
    #     assert_true(success, msg="dao-twitter登录")

    #
    # def test_wechat_login(self):
    #     poco_android.find_click(login_view.wx_login())
    #     air.sleep_dao(10)
    #     # poco_android.choose_zeus_user()
    #     # air.sleep(5)
    #     success = poco_unity.find(homes.menu_button())
    #     assert_true(success, msg="dao-wechat登录")
    #
    # def test_qq_login(self):
    #     # TODO:qq登录一直处于loading，需要后续修复
    #     poco_android.find_click(login_view.qq_login())
    #     air.sleep(3)
    #     poco_android.find_click(third_platform.qq_agree_btn())
    #     air.sleep(5)
    #     # poco_android.choose_zeus_user()
    #     # air.sleep(5)
    #     success = poco_unity.find(homes.menu_button())
    #     assert_true(success, msg="dao-qq登录")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        # 后置的清除账号操作
        parent, child = homes.logout_account()
        poco_unity.find_and_click_child_element(parent, child)
        # 结束时清空连接方便下次测试时初始化
        poco_unity.unity = None
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
