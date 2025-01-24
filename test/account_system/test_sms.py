import unittest

from retrying import retry

from page.account_system import base_dialog, login_view, sms, sms_verify
from page.game import welcome
from utils import air, poco_unity, poco_android
from utils.air import snapshot_screen
from utils.generates import generate_random_phone_number
from utils.logger import log
from airtest.core.api import *

class SmsTest(unittest.TestCase):
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

        poco_android.find_click(login_view.sms_login())

        pass

    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def test_sms_login_with_error_code(self):
        """dao-短信登录"""
        try:
            poco_android.set_text(sms.sms_phone_input(), generate_random_phone_number())
            poco_android.find_click(sms.send())
            # 等待 verify框的出现
            if poco_android.android(sms_verify.codes()).wait():
                snapshot_screen("验证码弹窗弹出成功")

                keyevent("TAB")
                keyevent("TAB")
                keyevent("TAB")
                keyevent("TAB")

                keyevent("13")
                keyevent("13")
                keyevent("13")
                keyevent("13")
                # poco_android.android(sms_verify.codes()).wait_for_disappearance(timeout=8)
                success = poco_android.find(sms_verify.codes())
                assert_true(success, msg="短信登录")
            else:
                # 发送验证码出错
                assert_true(False, msg="发送验证码出错")
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