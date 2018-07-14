import time
import os


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='solve_some_tags.log')
def solve_some_tags():
    url = "https://www.baidu.com/"

    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # 进入设置页面
    setting_elem = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(setting_elem).perform()
    search_settring_elem = driver.find_element_by_link_text("搜索设置")
    search_settring_elem.click()

    # 进行select标签的设置
    time.sleep(1)
    select_elem = driver.find_element_by_id("nr")
    Select(select_elem).select_by_index(2)

    driver.save_screenshot(os.getcwd() + '/selected.png')

    driver.quit()
    pass


if __name__ == '__main__':
    solve_some_tags()