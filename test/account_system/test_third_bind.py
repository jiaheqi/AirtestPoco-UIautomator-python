import unittest

from airtest.core.api import *
from airtest.core.assertions import assert_true, assert_false
from retrying import retry

from main import register_email_new_pre
from page.account_system import base_dialog, login_view, sms, sms_verify, email_login, email_verify
from page.game import  homes
from utils import air, poco_unity, dao_util, poco_android
from utils.generates import generate_random_phone_number
from utils.logger import log


class TestSmsBind(unittest.TestCase):
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

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_sms_bind(self):
        """dao-短信绑定"""
        parent, child = homes.sms_bind()
        poco_unity.find_and_click_child_element(parent, child)
        poco_android.set_text(sms.sms_phone_input(), generate_random_phone_number())
        poco_android.find_click(sms.send())
        success = poco_android.find(sms_verify.codes())
        if poco_android.android(sms_verify.codes()).wait():
            # 点两次TAB
            keyevent("TAB")
            keyevent("TAB")
            keyevent("TAB")
            keyevent("TAB")

            keyevent("13")
            keyevent("13")
            keyevent("13")
            keyevent("13")
            # poco_android.android(sms_verify.codes()).wait_for_disappearance(timeout=8)
            assert_true(success, msg="dao短信绑定")
        else:
            # 发送验证码出错
            assert_true(False, msg="发送验证码出错")

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_email_bind(self):
        """dao-邮箱绑定"""
        try:
            parent, child = homes.email_bind()
            poco_unity.find_and_click_child_element(parent, child)
            poco_android.set_text(email_login.email(), register_email_new_pre)
            poco_android.set_text(email_login.password(), "123456")
            poco_android.find_click(email_login.send())
            # disappear = poco_android.find(email_login.email())
            # success = not disappear
            success = poco_unity.find_child_element(parent, child)
            assert_true(success, msg="dao邮箱绑定")
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
