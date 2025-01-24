import unittest

from airtest.cli.parser import cli_setup
from airtest.core.api import device, auto_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco

from utils import zeus


class MyUITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化Airtest设备和Poco
        if not cli_setup():
            auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&", ])
        cls.poco = AndroidUiautomationPoco()
        cls.pocoUnity = UnityPoco()

    def test_example(self):
        # 编写测试用例，使用Poco进行UI操作
        self.pocoUnity(text="同意").click()
        self.poco(text="√").click()
        self.assertTrue(self.poco(text="√").exists(), "操作成功")

    # @classmethod
    # def tearDownClass(cls):
    #     # 关闭Airtest设备
    #     cls.airtest_device.stop()