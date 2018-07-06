import time


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def use_actionchains():
    index_url = "https://www.baidu.com/"
    # 无界面设置
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)

    # 模拟鼠标进行操作
    option_elem = driver.find_element_by_link_text('设置')
    ActionChains(driver).move_to_element(option_elem).perform() # 鼠标停留
    ActionChains(driver).move_to_element(option_elem).move_to_element() # 鼠标拖放
    ActionChains(driver).move_to_element(option_elem).context_click() # 鼠标单击
    ActionChains(driver).move_to_element(option_elem).double_click() # 鼠标双击
    # ActionChains(driver).move_to_element(option_elem).drag_and_drop(elem) # 拖放


if __name__ == '__main__':

    pass