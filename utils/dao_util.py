from page.game import homes
from utils import poco_unity


def open_account_center():
    """打开账号中心"""
    poco_unity.find_click(homes.menu_button())
    parent, child = homes.setting()
    print(parent, child)
    poco_unity.find_and_click_child_element(parent, child)
    btnAccount, title = homes.account_center()
    poco_unity.find_and_click_child_element(btnAccount, title)
