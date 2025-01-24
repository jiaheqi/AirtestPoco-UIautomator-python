from poco.drivers.ios import iosPoco

ios: iosPoco = None


def init_ios():
    global ios
    if ios is None:
        ios = iosPoco(use_airtest_input=True, screenshot_each_action=False)


def find(tmp):
    init_ios()
    return ios(tmp).exists()


def find_click(tmp):
    init_ios()
    if ios(tmp).exists():
        ios(tmp).click()
        return True
    else:
        return False


def set_text(ui: str, text: str):
    init_ios()
    if find(ui):
        ios(ui).set_text(text)


def find_no_click_index(tmp, index):
    init_ios()
    return ios(tmp)[index]


def find_no_click(tmp):
    init_ios()
    return ios(tmp)


def find_textMatches_click(text: str):
    init_ios()
    if ios(textMatches=text).exists():
        ios(textMatches=text).click()
        return True
    else:
        return False
