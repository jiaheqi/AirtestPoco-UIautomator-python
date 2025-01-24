# -*- encoding=utf8 -*-
__author__ = "CharlottePl"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554?",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
wait()


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


# script contentpoco("n4")
print("start...")

# poco("btnAgree").child("title").click()

poco("com.topjoy.dao:id/email").click()
poco("com.topjoy.dao:id/password").click()
poco("com.topjoy.dao:id/register").click()



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)




