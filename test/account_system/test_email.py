import unittest

from retrying import retry

from main import register_email_new_pre
from utils.logger import log
from utils import poco_android, poco_unity
from page.account_system import base_dialog, login_view, email_login, email_reset_password, email_verify, email_register
from utils import air
from airtest.core.api import *
from page.game import welcome, homes
import random


class EmailTest(unittest.TestCase):
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
        # 添加等待，提高准确性
        air.sleep_dao(3)
        poco_android.find_click(login_view.email_login())
        air.sleep_dao(3)

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_login(self):
        """dao-邮箱登录"""
        try:
            poco_android.set_text(email_login.email(), "charlotteplczy@gmail.com")
            poco_android.set_text(email_login.password(), "123456")
            poco_android.find_click(email_login.send())
            air.sleep_dao(2)
            poco_android.choose_zeus_user()
            air.sleep(15)
            success = poco_unity.find(homes.menu_button())
            assert_true(success, msg="dao-邮箱登录")
        except Exception as e:
            log(e)
            raise Exception

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_reset_password(self):
        """dao-邮箱重置密码"""
        try:
            # 点击忘记密码
            if poco_android.find_click(email_login.reset_password()) is False:
                # 断言 没找到按钮
                if poco_android.find_textMatches_click("忘记密码") is False:
                    # assert_true(False, msg="没找到 重置密码 按钮")
                    touch(Template(r"sources/pics/resetpassword.png", record_pos=(-0.313, 0.178), resolution=(900, 1600) ,threshold=0.2))
            poco_android.set_text(email_reset_password.email(), "charlotteplczy")
            poco_android.set_text(email_reset_password.password(), "123456")
            poco_android.set_text(email_reset_password.password_(), "123456")

            poco_android.find_click(email_reset_password.send())

            # 等待 verify框的出现
            if poco_android.android(email_verify.codes()).wait():
                # 点两次TAB
                keyevent("TAB")
                keyevent("TAB")
                keyevent("TAB")

                keyevent("13")
                keyevent("13")
                keyevent("13")
                keyevent("13")
                air.sleep_dao(1)
                success = poco_android.find(email_verify.codes())
                assert_true(success, msg="dao-重置密码")
        except Exception as e:
            log(e)
            raise Exception

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_register(self):
        """dao-邮箱注册"""
        try:
            if poco_android.find_click(email_login.register()) is False:
                poco_android.find_click(email_login.register())
                # 断言 没找到按钮
                if poco_android.find_text_click("去注册") is False:
                    # assert_true(False, msg="没找到 去注册 按钮")
                    touch(Template(r"sources/pics/register.png", record_pos=(0.318, 0.178), resolution=(900, 1600), threshold=0.2))
            poco_android.set_text(email_register.email(), register_email_new_pre)
            poco_android.set_text(email_register.password(), "123456")
            poco_android.set_text(email_register.password_(), "123456")
            poco_android.find_click(email_register.send())
            air.sleep_dao(8)
            success = poco_unity.find(homes.menu_button())
            assert_true(True, msg="dao-邮箱注册")
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
