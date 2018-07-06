from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def use_keys():
    index_url = 'https://www.baidu.com/'
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)

     # 进行搜索
    search_elem = driver.find_element_by_id("kw")
    search_elem.send_keys(Keys.BACK_SPACE) # 键盘回车
    search_elem.send_keys(Keys.CONTROL, 'a') # 全选当前焦点区域
    search_elem.send_keys(Keys.CONTROL, 'c') # 复制当前焦点区域
    search_elem.send_keys(Keys.CONTROL, 'v') # 粘贴当前焦点区域
    pass


if __name__ == '__main__':
    pass