import time

from selenium import webdriver

def search_use_baidu():
    # 设置浏览器
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    url = "https://www.baidu.com/"
    driver.get(url)

    # 输入搜索
    # search_elem = driver.find_element_by_name("word")
    print(driver.page_source)


def search_woyaozixue():
    url = "http://www.51zxw.net/"

    # 配置无界面chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # 搜索
    search_elem = driver.find_element_by_name("sgo")
    search_elem.send_keys("ps")

    click_elem = driver.find_element_by_class_name("search_btn")
    click_elem.click()

    print(driver.page_source)

if __name__ == '__main__':
    search_use_baidu()
    # search_woyaozixue()