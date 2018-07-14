import os
import time


from selenium import webdriver


def get_cookie():
    index_url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=java&rsv_pq=dc64725e0003a4c0&rsv_t=c5229xzgMvm6FgnHHS0EQCL2j3%2F3UsnshwCdljrA4wnmZoIxzI10UhfhU%2BU&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=706&rsv_sug4=2093"

    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)

    # 输出cookies
    print(driver.get_cookies())

    # 添加cookie（实际上是修改cookie）
    driver.add_cookie({'name' : 'luzulin', 'value' : 'hello'})
    print(driver.get_cookies())

    # 捉取制定的cookie
    name = driver.get_cookie("luzulin")
    print(name)

    pass


if __name__ == '__main__':
    get_cookie()