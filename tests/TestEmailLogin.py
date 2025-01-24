# -*- encoding=utf8 -*-
__author__ = "jiaheqi"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.report.report import simple_report
from poco.drivers.unity3d import UnityPoco

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&", ])
start_app("com.topjoy.dao")
sleep(7)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
pocoUnity = UnityPoco()
# pocoUnity(text="同意").click()
touch(Template(r"../sources/pics/tpl1699512397262.png", record_pos=(-0.007, 0.367), resolution=(1080, 2400)))
poco(text="√").click()
# poco("android.widget.FrameLayout").offspring("android:id/content").offspring(
#     "com.topjoy.dao:id/login_view_small").child("android.widget.ImageView")[1].click()
touch(Template(r"../sources/pics/tpl1699512411722.png", record_pos=(0.14, -0.013), resolution=(1080, 2400)))
sleep(3)
poco("com.topjoy.dao:id/email").click()
poco("com.topjoy.dao:id/email").set_text("jiaheqi@topjoy.com")
poco("com.topjoy.dao:id/password").click()
poco("com.topjoy.dao:id/password").set_text("1234")
poco("com.topjoy.dao:id/send").click()
poco("android.widget.FrameLayout").offspring("android:id/content").offspring(
    "com.topjoy.dao:id/select_user_list").child("android.widget.LinearLayout")[0].offspring(
    "com.topjoy.dao:id/mc_select_user_item_img")[0].click()
sleep(5)
assert_exists(Template(r"../sources/pics/tpl1699513869135.png",
                       record_pos=(-0.001, 0.79), resolution=(1080, 2400)), "邮箱登录游戏成功")
simple_report(__file__, logpath=True)

