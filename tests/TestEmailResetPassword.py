# -*- encoding=utf8 -*-
__author__ = "jiaheqi"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco

# 密码重置
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&", ])
start_app("com.topjoy.dao")
sleep(7)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
pocoUnity = UnityPoco()
# pocoUnity(text="同意").click()
touch(Template(r"../sources/pics/tpl1699512397262.png", record_pos=(-0.007, 0.367), resolution=(1080, 2400)))
poco(text="√").click()
touch(Template(r"../sources/pics/tpl1699512411722.png", record_pos=(0.14, -0.013), resolution=(1080, 2400)))
# poco("android.widget.FrameLayout").offspring("android:id/content").offspring(
#     "com.topjoy.dao:id/login_view_small").child("android.widget.ImageView")[3].click()
sleep(3)
poco("com.topjoy.dao:id/find_password").click()
poco("com.topjoy.dao:id/email").click()
poco("com.topjoy.dao:id/email").set_text("jiaheqi@topjoy.com")
poco("com.topjoy.dao:id/password").click()
poco("com.topjoy.dao:id/password").set_text("1234")
poco("com.topjoy.dao:id/password_").click()
poco("com.topjoy.dao:id/password_").set_text("1234")
poco("com.topjoy.dao:id/send").click()
poco("com.topjoy.dao:id/codes").click()
poco("com.topjoy.dao:id/codes").set_text("1111")
assert poco(name="验证失败，请重试").exists(), "弹窗未提示"
