import time
import os


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def solve_baidu():
    url = "https://www.baidu.com/"
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # 在设置elem上悬浮
    setting_elem = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(setting_elem).perform()

    # 选中搜索设置
    search_elem = driver.find_element_by_link_text("搜索设置")

    # 操作设置页面
    search_elem.click()
    time.sleep(3)
    save_setting_elem = driver.find_element_by_class_name("prefpanelgo").click()

    # 解决弹出框
    # time.sleep(3)
    # driver.save_screenshot(os.getcwd() + '/before.png')
    driver.switch_to.alert.accept()
    driver.close()
    time.sleep(1)
    driver.save_screenshot(os.getcwd() + '/after.png')  # 此时无法使用该功能？
    driver.quit()
    pass



if __name__ == '__main__':
    solve_baidu()