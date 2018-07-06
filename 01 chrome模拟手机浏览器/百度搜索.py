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
    # time.sleep(3)
    # search_elem = driver.find_element_by_id("index-kw")
    search_xpath = "//form[@id='index-form']"
    search_elem = driver.find_element_by_xpath(search_xpath)
    print(search_elem)
    # search_elem.send_keys("python")
    # print(search_elem)

if __name__ == '__main__':
    search_use_baidu()
