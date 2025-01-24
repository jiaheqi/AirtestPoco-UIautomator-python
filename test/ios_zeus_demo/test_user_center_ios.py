import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_base, demo_user_center, third_platform, menu_third, check
from page.zeus_demo.demo_user_center import bind_and_unbind, restart
from utils import air, poco_android, poco_ios
from utils.logger import log


class UserCenterTest(unittest.TestCase):
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
        poco_ios.find_click("用户中心")

    def test_apple_bind_and_unbind(self):
        """用户中心：apple绑定/解绑"""
        poco_ios.find_click("绑定/解绑")
        poco_ios.find_click("Sign in with Apple")
        success = poco_ios.find_no_click("解绑")
        assert_true(success, msg="ios用户中心-apple绑定")
        poco_ios.find_click("Sign in with Apple")
        success = poco_ios.find_no_click("绑定")
        assert_true(success, msg="ios用户中心-apple解绑")

    def test_facebook_bind_and_unbind(self):
        """用户中心：facebook绑定/解绑"""
        poco_ios.find_click("绑定/解绑")
        poco_ios.find_click("Facebook")
        success = poco_ios.find_no_click("解绑")
        assert_true(success, msg="ios用户中心-facebook绑定")
        poco_ios.find_click("Facebook")
        success = poco_ios.find_no_click("解绑")
        assert_true(success, msg="ios用户中心-apple解绑")

    def test_twitter_bind_and_unbind(self):
        """用户中心：twitter绑定/解绑"""
        air.sleep_zeus_demo(5)
        poco_android.find_text_click(bind_and_unbind())
        poco_android.find_click(demo_user_center.twitter_bind())
        air.sleep_zeus_demo(5)
        poco_android.find_click(third_platform.twitter_ok_btn())
        air.sleep_dao(2)
        if poco_android.get_text(demo_user_center.twitter_bind()) == '解绑':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-twitter绑定")
        poco_android.find_click(demo_user_center.twitter_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        poco_android.find_click(third_platform.twitter_ok_btn())
        if poco_android.get_text(demo_user_center.twitter_bind()) == '去绑定':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-twitter解绑")

    def test_restart(self):
        """用户中心：重新开始"""
        poco_android.find_text_click(restart())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.restart_confirm())
        air.sleep_zeus_demo(2)
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="用户中心-重新开始")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
