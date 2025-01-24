import unittest

from airtest.core.assertions import assert_true
from utils import air, poco_ios
from utils.logger import log
from utils.poco_ios import ios


class InitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 初始化")
        pass

    def setUp(self):
        method_name = self._testMethodName
        log(f"{method_name} - 准备")
        # 启动demo并初始化
        air.stop_zeus_demo_ios()
        air.start_zeus_demo_ios()

    def test_init(self):
        """"""
        poco_ios.find_click("初始化")
        success = poco_ios.find("resultCode:1")
        assert_true(success, msg="初始化")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
