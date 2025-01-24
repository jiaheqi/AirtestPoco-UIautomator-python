# -*- encoding=utf8 -*-
__author__ = "jiaheqi"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco

# 手机短信登录，验证码错误
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&", ])
stop_app("com.topjoy.dao")
start_app("com.topjoy.dao")
sleep(7)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
pocoUnity = UnityPoco()
# pocoUnity(text="同意").click()
touch(Template(r"../sources/pics/tpl1699512397262.png", record_pos=(-0.007, 0.367), resolution=(1080, 2400)))
poco(text="√").click()
poco("android.widget.FrameLayout").offspring("android:id/content").offspring(
    "com.topjoy.dao:id/login_view_small").child("android.widget.ImageView")[3].click()
sleep(3)
# touch(Template(r"../sources/pics/tpl1699610166873.png", record_pos=(0.002, 0.03), resolution=(900, 1600)))
poco("com.topjoy.dao:id/ed_phone_number").click()
poco("com.topjoy.dao:id/ed_phone_number").set_text("17600116844")
poco("com.topjoy.dao:id/btn_send").click()
poco("com.topjoy.dao:id/codes").click()
poco("com.topjoy.dao:id/codes").set_text("1111")
assert poco(name="验证失败，请重试").exists(), "弹窗未提示"
simple_report(__file__, logpath=True)