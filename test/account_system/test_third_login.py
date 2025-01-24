import unittest

from retrying import retry

from page.zeus_demo import third_platform
from utils.generates import generate_random_email
from utils.logger import log
from utils import poco_android, poco_unity
from page.account_system import base_dialog, login_view, email_login, email_reset_password, email_verify, email_register
from utils import air
from airtest.core.api import *
from page.game import welcome, homes
import random


class ThirdLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")

        # 关闭APP
        air.stop_dao()

        # 清除APP 数据
        air.clear_dao()

        # 打开APP
        air.start_dao()

        # 等待DAO完全启动
        air.sleep_dao(15)
        if poco_android.find_click(base_dialog.agree()) is not True:
            touch(Template(r"sources/pics/loginviewagree.png", record_pos=(-0.218, 0.217), resolution=(900, 1600), threshold=0.3))

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
    # @retry(stop_max_attempt_number=3, wait_fixed=3000)
    # def test_twitter_login(self):
    #     """dao-twitter登录"""
    #     try:
    #         poco_android.find_click(login_view.twitter_login())
    #         air.sleep(5)
    #         poco_android.find_click(third_platform.twitter_ok_btn())
    #         air.sleep(10)
    #         success = poco_unity.find(homes.menu_button())
    #         assert_true(success, msg="dao-twitter登录")
    #     except Exception as e:
    #         log(e)
    #         raise Exception

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
    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_guest_login(self):
        """dao-游客登录"""
        try:
            poco_android.find_click(login_view.guest_login())
            air.sleep(5)
            success = not poco_android.find(login_view.guest_login())
            assert_true(success, msg="dao-游客登录")
        except Exception as e:
            log(e)
            raise Exception

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        # 结束时清空连接方便下次测试时初始化
        poco_unity.unity = None
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
