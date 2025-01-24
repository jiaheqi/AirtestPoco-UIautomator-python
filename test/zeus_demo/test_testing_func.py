import unittest

from airtest.core.assertions import assert_true
from retrying import retry

from page.zeus_demo import menu_init, menu_test, check
from utils import air, poco_android
from utils.logger import log


class TestFuncTest(unittest.TestCase):
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
        air.sleep_zeus_demo(3)
        poco_android.find_click(menu_init.menu_init())
        poco_android.find_click(menu_init.init())
        poco_android.find_click(menu_test.menu_test())

    def test_get_skuList(self):
        """google获取商品列表"""
        poco_android.find_click(menu_test.sku_list())
        success = poco_android.find(check.zeus_yes())
        assert_true(success, msg="获取谷歌商品列表skuList")

    def tearDown(self):
        method_name = self._testMethodName
        log(f"{method_name} - 结束")
        pass

    @classmethod
    def tearDownClass(cls):
        class_name = cls.__name__
        log(f"{class_name} - 结束")
