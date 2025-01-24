import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_base, demo_user_center, third_platform, menu_third, check
from page.zeus_demo.demo_user_center import bind_and_unbind, restart
from utils import air, poco_android
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
        air.stop_zeus_demo()
        air.start_zeus_demo()
        air.sleep_zeus_demo(5)
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.menu_base())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.clear_user_account())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.login())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_base.user_center())

    def test_google_bind_and_unbind(self):
        """用户中心：谷歌绑定/解绑"""
        poco_android.find_text_click(bind_and_unbind())
        poco_android.find_click(demo_user_center.google_bind())
        poco_android.find_click(third_platform.google_select_account())
        if poco_android.get_text(demo_user_center.google_bind()) == '解绑':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-谷歌绑定")
        poco_android.find_click(demo_user_center.google_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        poco_android.find_click(third_platform.google_select_account())
        if poco_android.get_text(demo_user_center.google_bind()) == '去绑定':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-谷歌解绑")

    def test_facebook_bind_and_unbind(self):
        """用户中心：facebook绑定/解绑"""
        poco_android.find_text_click(bind_and_unbind())
        poco_android.find_click(demo_user_center.facebook_bind())
        air.sleep_zeus_demo(10)
        if poco_android.get_text(demo_user_center.facebook_bind()) == '解绑':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-facebook绑定")
        poco_android.find_click(demo_user_center.facebook_bind())
        air.sleep_zeus_demo(2)
        poco_android.find_click(menu_third.unbind_confirm())
        air.sleep_zeus_demo(10)
        if poco_android.get_text(demo_user_center.facebook_bind()) == '去绑定':
            success = True
        else:
            success = False
        assert_true(success, msg="用户中心-facebook解绑")

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

