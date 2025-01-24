# -*- encoding=utf8 -*-
__author__ = "DELL"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco

# 手机绑定，验证码错误
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&",])
poco1 = UnityPoco()
print("start...")
# poco1("UIGMBtn").click()
# poco1("func2").click()
# poco1("btnSkipGuide").click()
# poco1("close").child("n0").click()
poco1("n3").click()
poco1("settingBtn").child("title").click()
sleep(2)
# poco1("btnAccount").click()
# poco1("Item2Comp").click()
touch(Template(r"../sources/pics/tpl1699613261877.png", record_pos=(0.294, 0.268), resolution=(900, 1600)))
touch(Template(r"../sources/pics/tpl1699613266821.png", record_pos=(0.004, -0.018), resolution=(900, 1600)))


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco("com.topjoy.dao:id/ed_phone_number").click()
poco("com.topjoy.dao:id/ed_phone_number").set_text("17600116843")
poco("com.topjoy.dao:id/btn_send").click()
poco("com.topjoy.dao:id/codes").click()
keyevent("1")
keyevent("1")
keyevent("1")
keyevent("1")
# pyautogui.write("1111")
# poco("com.topjoy.dao:id/codes").set_text("1111")
assert poco(name="验证失败，请重试").exists(), "弹窗未提示"
simple_report(__file__, logpath=True)