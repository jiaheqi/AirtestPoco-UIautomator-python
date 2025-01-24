# import unittest
#
# from page.account_system import base_dialog, login_view
# from page.game import homes
# from utils import air, poco_unity, poco_android
# from utils.logger import log
#
#
# class ThirdLoginTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         class_name = cls.__name__
#         log(f"{class_name} - 初始化")
#
#     def setUp(self):
#         method_name = self._testMethodName
#         log(f"{method_name} - 准备")
#         # 关闭APP
#         air.stop_dao()
#
#         # 清除APP 数据
#         air.clear_dao()
#
#         # 打开APP
#         air.start_dao()
#
#         # 等待DAO完全启动
#         air.sleep_dao(15)
#
#         poco_android.find_click(base_dialog.agree())
#
#         poco_android.find_click(login_view.google_login())
#         air.sleep(3)
#         poco_android.find_text_click("charlotteplczy@gmail.com")
#         air.sleep(5)
#
#     def test_google_pay(self):
#         """谷歌支付"""
#         parent, child = homes.open_store()
#         poco_unity.find_and_click_child_element(parent, child)
#
#     def tearDown(self):
#         method_name = self._testMethodName
#         log(f"{method_name} - 结束")
#         # 结束时清空连接方便下次测试时初始化
#         poco_unity.unity = None
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         class_name = cls.__name__
#         log(f"{class_name} - 结束")
