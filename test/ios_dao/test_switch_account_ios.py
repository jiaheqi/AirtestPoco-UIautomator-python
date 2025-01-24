import unittest

from retrying import retry

from page.game import homes
from utils import air, dao_util, poco_unity, poco_ios
from utils.zeus import log, login_view
from airtest.core.api import *


class SwitchAccountLoginTest(unittest.TestCase):
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
        air.sleep(10)
        poco_ios.find_click("selectno")
        poco_ios.find_click("user2")
        air.sleep(5)
        dao_util.open_account_center()
        parent, child = homes.switch_account()
        poco_unity.find_and_click_child_element(parent, child)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_switch_email_login(self):
        """ios切换账号邮箱登录"""
        try:
            poco_ios.find_click("selectno")
            poco_ios.find_click("iconemail")
            poco_ios.find_click("TextField")
            air.text("jiaheqi@topjoy.com")
            poco_ios.find_click("SecureTextField")
            air.text("1234")
            poco_ios.find_click("登录")
            touch(Template(r"sources/pics/selectzeusaccount.png", rgb=True, record_pos=(-0.213, -0.249),
                           resolution=(1124, 2436), threshold=0.3))
            air.sleep(2)
            parent, child = homes.logout_account()
            success = poco_unity.find_child_element(parent, child)
            assert_true(success, msg="dao-ios切换账号邮箱登录")
        except Exception as e:
            log(e)
            raise Exception

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        # 后置的清除账号操作
        air.sleep(2)
        parent, child = homes.logout_account()
        poco_unity.find_and_click_child_element(parent, child)
        # 结束时清空连接方便下次测试时初始化
        poco_unity.unity = None
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")