from time import sleep, time

from airtest.cli.parser import cli_setup
from airtest.core.api import device, auto_setup
from appium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from conf import ids


def log(logs):
    print('  ', logs)


def start():
    global driver
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', parms)
    log("- 创建 driver ...")
    driver = webdriver.Remote('http://192.168.156.147:4723/wd/hub', parms)
    # driver = webdriver.Remote('http://localhost:4723/', parms)
    driver.implicitly_wait(10)  # 默认等待时间


def init_devices():
    # global airtest_device
    # airtest_device = device()
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/49f2f609?touch_method=MAXTOUCH&", ])


# 滑动屏幕
def swipe(sx, sy, ex, ey, time):
    driver.swipe(sx, sy, ex, ey, time)


def swipe():
    driver.swipe(839, 1112, 824, 456, 800)


def back():
    driver.keyevent(4)


# 初始化
msg = 'dao测试日志'
pkg = 'com.topjoy.dao'
activity = 'com.topjoy.dao.UnityPlayerActivity'
avd = 'emulator-5554'
online = ''
# 初始化参数
parms = {
    'platformName': 'Android',  # 被测设备系统
    'platformVersion': '13',  # OS Version
    'newCommandTimeout': "6000",  # 超时时间
    'deviceName': '49f2f609',  # Device Name
    'appPackage': pkg,  # APP PackageName
    'appActivity': activity,  # APP LaunchActivity
    'unicodeKeyboard': False,  # Chinese
    'noReset': True,  # Not Reset APP
    'automationName': 'UiAutomator2',
    # 'app' : r'd:\apk\bili.apk,
}
driver = None


# 检查测试结果
def check():
    log('- 检查结果')
    try:
        # 等待yes出现
        if find(ids.id_zeus_yes):
            f = find(ids.id_zeus_yes)
            flag = f.get_attribute("text")
        else:
            return False

        for i in range(0, 20):
            if flag == 'waitting':
                sleep(1)
                flag = f.get_attribute("text")
                continue
            break

        return flag == "success"
    except NoSuchElementException:
        return False


def get_status_text(driver, timeout=10):
    """检查测试结果"""
    log('- 检查结果')
    # 等待yes出现
    start_time = time.time()
    f = find(ids.id_zeus_yes)
    status_text = f.get_attribute("text")

    while status_text == 'waitting' and time.time() - start_time < timeout:
        log("still waitting...")
        time.sleep(1)
        status_text = f.get_attribute("text")
    log(str(status_text) + '\n')
    return str(status_text) == "success"


# 等待元素出现
def find(item):
    try:
        eve = driver.find_element(By.ID, item)
        return eve
    except NoSuchElementException:
        return None


# 等待元素出现并点击
def findClick(item):
    flag = False
    try:
        btn = driver.find_element(By.ID, item)
        btn.click()
        flag = True
    except NoSuchElementException:
        flag = False
    finally:
        return flag


#
#
# def wait(driver, item, timeout=10):
#     """等待元素出现"""
#     try:
#         return WebDriverWait(driver, timeout).until(lambda x: x.find_element(By.ID, item))
#     except TimeoutException:
#         # TODO 这里给手机截个图？
#         log("wait for " + item + " timeout")
#         raise TimeoutException
#
#
# 等待元素出现
def findByXPath(item):
    try:
        eve = driver.find_element(By.XPATH, item)
        return eve
    except NoSuchElementException:
        return None


def findByCoordinateAndClick(x, y):
    driver.tap([(x, y)])
    sleep(10)


def agree_view():
    log('- 同意用户协议 ...')
    findByCoordinateAndClick(ids.x_agree_view, ids.y_agree_view)


def login_view():
    agree_view()


def login_view_google():
    log('- 开始测试 login_view_google登录...')
    login_view()
    log('- 选择登录方式 google登录...')
    findByXPath(ids.x_login_view_google).click()
    if findByXPath(ids.x_google_user) is not None:
        findByXPath(ids.x_google_user).click()
    sleep(5)
    if findByXPath(ids.x_zeus_select_user):
        findByXPath(ids.x_zeus_select_user).click()


def login_view_facebook():
    pass


def login_view_email():
    log('- 开始测试 login_view_email登录...')
    login_view()
    log('- 选择登录方式 email登录...')
    findByXPath(ids.x_login_view_email).click()

    sleep(5)
    if findByXPath(ids.x_zeus_select_user):
        findByXPath(ids.x_zeus_select_user).click()
