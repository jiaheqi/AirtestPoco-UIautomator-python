import concurrent
import re
import subprocess
import concurrent.futures
import unittest
from unittest import TestSuite

from unittestreport import TestRunner

from utils import notify
from utils.generates import generate_random_email_prefix
from utils.logger import log
from airtest.core.api import *
import os
import datetime

report_path = "./report"
log_path = "./log"
sdkPwd = '/Users/jenkins/library/Android/sdk/tools'
adb_tool_path = '/Users/jenkins/Library/Android/sdk/platform-tools/adb'
apk_path = "./conf/launcher-debug.apk"
global register_email_new_pre
register_email_new_pre = generate_random_email_prefix()


# adb_tool_path = 'adb'

def get_report_path(device):
    # global report_path
    now = datetime.datetime.now()
    year = now.year
    date = now.strftime("%m%d")
    device = format_device_name(device)
    # 创建设备特定的 report 目录
    device_report_path = os.path.join(report_path, device, str(year), date)
    if not os.path.exists(device_report_path):
        os.makedirs(device_report_path)

    # 获取当前设备目录下的报告数
    device_reports = os.listdir(device_report_path)
    num = len([f for f in device_reports if f.startswith("report")])
    # 输出当前报告应该存放的路径
    return os.path.join(device_report_path, f"report_{num}.html")


def get_log_path(device):
    # global log_path
    now = datetime.datetime.now()
    year = now.year
    date = now.strftime("%m%d")
    device = format_device_name(device)
    # 创建设备特定的 log 目录
    device_log_path = os.path.join(log_path, device, str(year), date)
    if not os.path.exists(device_log_path):
        os.makedirs(device_log_path)

    # 获取当前设备目录下的文件夹数
    device_folders = [f for f in os.listdir(device_log_path) if os.path.isdir(os.path.join(device_log_path, f))]
    num = len(device_folders)
    device_log_path = os.path.join(device_log_path, str(num))
    if not os.path.exists(device_log_path):
        os.makedirs(device_log_path)

    # 输出当前日志应该存放的路径
    return device_log_path


def format_device_name(device):
    # 替换特殊字符为下划线
    return re.sub(r'[^a-zA-Z0-9._-]', '_', device)


def start_emu():
    # restart emulator
    start = 'nohup /Users/jenkins/Library/Android/sdk/emulator/emulator -avd auto -netdelay none -netspeed full -no-snapshot-save -snapshot 0210 -no-boot-anim  &'
    os.system(start)


def kill_emu():
    # kill emulator
    kill = '/Users/jenkins/Library/Android/sdk/platform-tools/adb emu kill'
    os.system(kill)


def start_Nox():
    # restart emulator
    log('- 开启Nox')
    start = 'nohup open -a NoxAppPlayer &'
    os.system(start)


def kill_Nox():
    log('- 关闭Nox')
    # kill emulator
    kill = 'killall NoxAppPlayer'
    os.system(kill)


def get_running_emulators(adb_path):
    try:
        output = subprocess.check_output(['adb', 'devices'], universal_newlines=True)
        # 分割输出为行
        lines = output.strip().split('\n')

        # 跳过第一行（标题）
        devices = lines[1:]

        # 提取模拟器设备信息
        # emulators = [device.split()[0] for device in devices if '127' in device]
        emulators = devices[0].rstrip('\tdevice')

        return emulators
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


def install_apk(adb_path, apk_path):
    try:
        # 构建安装命令
        install_command = [adb_path, '-s', get_running_emulators(adb_tool_path)[0], 'install', '-r', apk_path]

        # 执行安装命令
        subprocess.run(install_command, check=True)
        print("APK 安装成功！")
    except subprocess.CalledProcessError as e:
        print(f"安装失败: {e}")


def start_xcode_test():
    """启动xcoce并在设备上运行wda的方法"""
    try:
        wda_path = '/Users/topjoy/ios/WebDriverAgent/WebDriverAgent.xcodeproj'
        xcodebuild_path = 'xcodebuild'
        device_uuid = '1d96e59cd91c1363ce9756eca143cb041373a1a6'
        subprocess.run(
            [xcodebuild_path, '-project', wda_path, '-scheme', 'WebDriverAgentRunner', '-destination',
             f'id={device_uuid}',
             'test'])
    except Exception as e:
        print(f"Exception in start_xcode_test: {e}")


def merge_html_reports(report_files, output_file):
    merged_content = ""
    for report_file in report_files:
        with open(report_file, 'r') as f:
            content = f.read()
            merged_content += content

    with open(output_file, 'w') as f:
        f.write(merged_content)


def run_android():
    # 打开模拟器
    # kill_emu()
    # start_emu()
    # sleep(60)
    # kill_Nox()
    # start_Nox()
    # sleep(60)
    # install_apk('',apk_path)
    # sleep(60)
    running_emulators = get_running_emulators(adb_tool_path)
    print(running_emulators)
    # device = running_emulators
    device = 'emulator-5554'
    print(register_email_new_pre)
    # 特别注意，游戏应用的Poco初始化，都应该放在游戏启动之后才能进行！！！
    log('初始化Poco')
    auto_setup(__file__, logdir=log_path, devices=[f"Android:///{device}"])
    current_dir = os.getcwd()
    # start_dir = os.path.join(current_dir, 'test/account_system/')
    start_dir = 'test/account_system/'
    print(current_dir)
    print(start_dir)
    pattern = "test_*.py"
    # 如果demo测试添加重试，dao测试不重试
    # count和interval属性进行重试操作
    if start_dir == 'test/zeus_demo/':
        count = 3
        interval = 3
    else:
        count = 0
        interval = 0
    suite = TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir, pattern)
    suite.addTest(testcases)
    runner = TestRunner(suite=suite,
                        filename="uiauto_report_android.html",
                        report_dir="./report",
                        title='UI自动化测试报告android',
                        tester='uiauto',
                        desc="zeusUI自动化测试生成的报告android",
                        )
    runner.rerun_run(count=count, interval=interval)
    # simple_report(__file__, logpath=log_path, output=report_path)
    # notify.send_mail()


def run_ios():
    log('初始化Poco')
    device = "169.254.69.14"
    device_ip = f"http://{device}:8100"
    auto_setup(__file__, logdir=log_path, devices=[f"ios:///{device_ip}"])
    # auto_setup(__file__, logdir=log_path, devices=["ios:///http+usbmux://1d96e59cd91c1363ce9756eca143cb041373a1a6"
    #                                                ":8100?mjpeg_port=9100",])
    log("设备初始化成功")
    current_dir = os.getcwd()
    # start_dir = os.path.join(current_dir, 'test/ios_dao/')
    start_dir = 'test/ios_dao/'
    print(current_dir)
    print(start_dir)
    pattern = "test_a_email_register.py"
    # 如果demo测试添加重试，dao测试不重试
    # count和interval属性进行重试操作
    if start_dir == 'test/ios_zeus_demo/':
        count = 3
        interval = 3
    else:
        count = 0
        interval = 0
    suite = TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir, pattern)
    suite.addTest(testcases)
    runner = TestRunner(suite=suite,
                        filename="uiauto_report_ios.html",
                        report_dir="./report",
                        title='UI自动化测试报告ios',
                        tester='uiauto',
                        desc="zeusUI自动化测试生成的报告ios",
                        )

    runner.rerun_run(count=count, interval=interval)
    # simple_report(__file__, logpath=log_path, output=report_path)
    # notify.send_mail()


def run_ios_and_android():
    log('初始化Poco，执行ios测试')
    device = "169.254.69.14"
    device_ip = f"http://{device}:8100"
    auto_setup(__file__, logdir=log_path, devices=[f"ios:///{device_ip}"])
    # auto_setup(__file__, logdir=log_path, devices=["ios:///http+usbmux://1d96e59cd91c1363ce9756eca143cb041373a1a6"
    #                                                ":8100?mjpeg_port=9100",])
    log("设备初始化成功")
    current_dir = os.getcwd()
    start_dir = os.path.join(current_dir, 'test/ios_dao/')
    pattern = "test_*.py"
    if start_dir == 'test/ios_zeus_demo/':
        count = 3
        interval = 3
    else:
        count = 0
        interval = 0
    suite = TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir, pattern)
    suite.addTest(testcases)
    runner = TestRunner(suite=suite,
                        filename="uiauto_report_ios.html",
                        report_dir="./report",
                        title='UI自动化测试报告ios',
                        tester='uiauto',
                        desc="zeusUI自动化测试生成的报告ios",
                        )

    runner.rerun_run(count=count, interval=interval)
    # running_emulators = get_running_emulators(adb_tool_path)
    # device = running_emulators
    device = '65TWJR5T7S4D6SMR'
    current_dir = os.getcwd()
    start_dir = os.path.join(current_dir, 'test/account_system/')
    pattern = "test_*.py"
    suite = TestSuite()
    # unitTest中的discover第三个参数top_level_dir第一次运行时如果为None会取当前传入的start_dir所在路径为top_level_dir
    # 而这个top_level_dir会作为self的参数保存下来，这样第二次运行时top_level_dir实际取的是上一次的路径，直接影响到了下一次的运行
    # 第二次需要手动将top_level_dir这个参数传给discover方法
    testcases = unittest.defaultTestLoader.discover(start_dir, pattern, top_level_dir=start_dir)
    suite.addTest(testcases)
    log('初始化Poco,执行安卓测试')
    auto_setup(__file__, logdir=log_path, devices=[f"Android:///{device}"])
    runner = TestRunner(suite=suite,
                        filename="uiauto_report_android.html",
                        report_dir="./report",
                        title='UI自动化测试报告android',
                        tester='uiauto',
                        desc="zeusUI自动化测试生成的报告android",
                        )
    runner.rerun_run(count=count, interval=interval)


def run():
    global report_path, log_path, register_email_new_pre
    run_ios_and_android()
    # run_ios()
    # run_android()
    notify.send_mail_multi()


if __name__ == '__main__':
    run()

