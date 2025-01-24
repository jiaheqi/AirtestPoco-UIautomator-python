from airtest.core.api import *

package_name = "com.topjoy.dao"
dao_iod_package_name = "com.topjoy.zeusdemo"
apk_path = "./conf/launcher-debug.apk"
zeus_demo_package_name = "com.topjoy.sdk_demo"
zeus_demo_apk_path = "./conf/app-debug.apk"
zeus_demo_ios_package_name = "com.topjoy.zeusdemo"


# 查找并点击tmp
def find_click(tmp):
    if exists(tmp):
        touch(tmp)
        return True
    else:
        return False


def start_dao():
    start_app(package_name)


def start_dao_ios():
    start_app(dao_iod_package_name)


def clear_dao():
    clear_app(package_name)


def stop_dao():
    stop_app(package_name)


def stop_dao_ios():
    stop_app(dao_iod_package_name)


def sleep_dao(time: int):
    sleep(time)


def install_dao():
    install(apk_path)


def wait_dao(tmp):
    wait(tmp, timeout=50)


def start_zeus_demo():
    start_app(zeus_demo_package_name)


def stop_zeus_demo():
    stop_app(zeus_demo_package_name)


def start_zeus_demo_ios():
    start_app(zeus_demo_ios_package_name)


def stop_zeus_demo_ios():
    stop_app(zeus_demo_ios_package_name)


def sleep_zeus_demo(time: int):
    sleep(time)


def clear_zeus_demo():
    clear_app(zeus_demo_package_name)


def snapshot_screen(tmp):
    snapshot(msg=tmp)


def keyEvent(key: str):
    keyEvent(key)
