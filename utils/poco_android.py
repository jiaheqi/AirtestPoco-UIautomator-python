from poco.drivers.android.uiautomation import AndroidUiautomationPoco

android: AndroidUiautomationPoco = None


def find_click(name: str):
    init_android()
    if android(name).exists():
        android(name).click()
        return True
    else:
        return False


def find_text_click(text: str):
    init_android()
    if android(text=text).exists():
        android(text=text).click()
        return True
    else:
        return False


def find_textMatches_click(text: str):
    init_android()
    if android(textMatches=text).exists():
        android(textMatches=text).click()
        return True
    else:
        return False


def find_type_click(type: str):
    init_android()
    if android(type=type).exists():
        android(type=type).click()
        return True
    else:
        return False


def find(tmp):
    init_android()
    return android(tmp).exists()


def set_text(ui: str, text: str):
    if find(ui):
        android(ui).set_text(text)


def init_android():
    global android
    if android is None:
        android = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def findAndClickHierarchy(*hierarchy):
    """在Poco中查找指定层级结构的元素并点击
    Args:
    poco: Poco实例
    hierarchy: 每个层级的信息，按照顺序传入，例如："android.widget.FrameLayout", "android:id/content", ...
    """

    element = android
    for level in hierarchy:
        # 对于子元素列表，使用child方法获取第一个子元素
        if isinstance(level, int):
            element = element.child(level)
        else:
            element = element.offspring(level)
    if element.exists():
        element.click()
    else:
        raise Exception("Element not found in the specified hierarchy")


def choose_zeus_user():
    """dao选择zeus用户"""
    try:
        if find_dao_select_user_list():
            android("android.widget.FrameLayout").offspring("android:id/content").offspring(
                "com.topjoy.dao:id/select_user_list").child("android.widget.LinearLayout")[0].offspring(
                "com.topjoy.dao:id/mc_select_user_item_img")[0].click()
        else:
            print("不需要选择zeus账户")
    except:
        print("不需要选择zeus账户")


def demo_choose_zeus_user():
    """zeus-demo选择zeus用户"""
    try:
        if find_demo_select_user_list():
            android("android.widget.FrameLayout").offspring("android:id/content").offspring(
                "com.topjoy.sdk_demo:id/select_user_list").child("android.widget.LinearLayout")[0].offspring(
                "com.topjoy.sdk_demo:id/mc_select_user_item_img")[0].click()
        else:
            print("不需要选择zeus账户")
            pass
    except:
        print("不需要选择zeus账户")
        pass


def find_demo_select_user_list():
    """判断是否需要选择zeus账号"""
    element = android("android.widget.FrameLayout").offspring("android:id/content").offspring(
        "com.topjoy.sdk_demo:id/select_user_list")
    if element.exists():
        return True
    else:
        return False


def find_dao_select_user_list():
    """判断是否需要选择zeus账号"""
    element = android("android.widget.FrameLayout").offspring("android:id/content").offspring(
        "com.topjoy.dao:id/select_user_list")
    if element.exists():
        return True
    else:
        return False


def get_text(name: str):
    init_android()
    if android(name).exists():
        return android(name).get_text()
    else:
        raise Exception("Element not found ")


def wx_pay_confirm():
    """微信支付立即支付"""
    android("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
        "android.widget.FrameLayout").offspring("android:id/content").offspring("com.tencent.mm:id/g3_").offspring(
        "com.tencent.mm:id/ccz").child("android.view.ViewGroup").child("android.view.ViewGroup").child(
        "android.view.ViewGroup")[1].click()


def ali_pay_finish():
    """支付宝支付完成"""
    android("android.widget.FrameLayout").offspring("android.widget.LinearLayout").child(
        "android.webkit.WebView").offspring("app").child("android.view.View")[6].click()


def ali_pay_input_password1():
    """第一次输入支付密码"""
    android("android.widget.FrameLayout").offspring("android.widget.LinearLayout").child(
        "android.webkit.WebView").child(
        "android.webkit.WebView").offspring("app").child("android.view.View")[8].click()


def ali_pay_input_password2():
    """第二次输入支付密码"""
    android("android.widget.FrameLayout").offspring("android.widget.LinearLayout").child(
        "android.webkit.WebView").child(
        "android.webkit.WebView").offspring("app").child("android.view.View")[4].click()
