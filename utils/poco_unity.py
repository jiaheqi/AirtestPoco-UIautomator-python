from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from page.game import homes
from page.account_system import base_dialog
from utils import air

unity: UnityPoco = None


def find_click(name: str):
    init_unity()
    if unity(name).exists():
        unity(name).click()
        return True
    else:
        return False


def find(tmp):
    init_unity()
    return unity(tmp).exists()


def init_unity():
    global unity
    if unity is None:
        unity = UnityPoco()


def wait_click(tmp):
    init_unity()


def swipe(name: str, pos: list):
    init_unity()
    if unity(name).exists():
        unity(name).swipe(pos)
        return True
    else:
        return False


def find_and_click_child_element(parent_name, child_name):
    """
    在Poco中查找指定父元素下的子元素并点击
    Args:
        parent_name: 父元素的名称
        child_name: 子元素的名称
    """
    init_unity()
    parent_element = unity(parent_name)
    child_element = parent_element.child(child_name)

    if child_element.exists():
        child_element.click()
    else:
        raise Exception(f"Child element '{child_name}' not found under '{parent_name}'")


def find_child_element(parent_name, child_name):
    """
    在Poco中查找指定父元素下的子元素
    Args:
        parent_name: 父元素的名称
        child_name: 子元素的名称
    """
    init_unity()
    parent_element = unity(parent_name)
    child_element = parent_element.child(child_name)

    if child_element.exists():
        return True
    else:
        return False


def skip_guide():
    """跳过引导"""
    # poco_unity.swipe(home.gm_button(), [0.2317, 0.3015])
    # poco_unity.find_click(home.gm_button())
    init_unity()
    air.find_click(base_dialog.gm_btn())
    find_click(homes.func_button())
    unity("UIGMPanel").offspring("btnSkipGuide").child("n0").click()
    unity("UIGMPanel").offspring("close").child("n0").click()
