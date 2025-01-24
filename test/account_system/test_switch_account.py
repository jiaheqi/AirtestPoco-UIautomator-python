import unittest

from retrying import retry

from main import register_email_new_pre
from utils.generates import generate_random_email_prefix
from utils.global_var import generate_email_pre
from utils.logger import log
from utils import poco_android, poco_unity, dao_util
from page.account_system import base_dialog, login_view, email_login, email_reset_password, email_verify, email_register
from utils import air
from airtest.core.api import *
from page.game import welcome, homes
import random


class SwitchAccountTest(unittest.TestCase):
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

        # 同意隐私协议
        # poco_unity.find_click(welcome.agree())

        if poco_android.find_click(base_dialog.agree()) is not True:
            touch(Template(r"sources/pics/loginviewagree.png", record_pos=(-0.218, 0.217), resolution=(900, 1600), threshold=0.3))

        poco_android.find_click(login_view.guest_login())
        air.sleep_dao(10)
        dao_util.open_account_center()
        air.sleep_dao(5)
        parent, child = homes.switch_account()
        poco_unity.find_and_click_child_element(parent, child)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_switch_account_email_login(self):
        """dao-切换账号邮箱登录"""
        try:
            poco_android.find_click(base_dialog.agree())
            poco_android.find_click(login_view.email_login())
            air.sleep_dao(3)
            poco_android.set_text(email_login.email(), "charlotteplczy@gmail.com")
            poco_android.set_text(email_login.password(), "123456")
            poco_android.find_click(email_login.send())
            air.sleep_dao(2)
            poco_android.choose_zeus_user()
            air.sleep(5)
            parent, child = homes.logout_account()
            success = poco_unity.find_child_element(parent, child)
            assert_true(success, msg="dao-切换账号邮箱登录")
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
