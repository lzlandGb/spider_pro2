import os
import time


from selenium import webdriver


def use_js():
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=java&oq=python&rsv_pq=e3a13cb40002e950&rsv_t=759feqgyEU4fWGKnkoaXozanXlsLq9CgOADG38vz8eU5nmxn%2F1WrEjx9szI&rqlang=cn&rsv_enter=1&inputT=1949&rsv_sug3=16&rsv_sug1=15&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1949"

    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # 进行搜索
    search_elem = driver.find_element_by_id("kw")
    search_elem.clear()
    search_elem.send_keys("php")
    search_btn_elme = driver.find_element_by_id("su").click()

    # 进行js操作
    time.sleep(2)
    driver.save_screenshot(os.getcwd() + "/normal_search.png")
    js = "window.scrollTo(200, 550);"
    driver.execute_script(js)
    time.sleep(1)
    driver.save_screenshot(os.getcwd() + '/active_search.png') # 调用js，也可以使用现成的js代码
    pass


if __name__ == '__main__':
    use_js()