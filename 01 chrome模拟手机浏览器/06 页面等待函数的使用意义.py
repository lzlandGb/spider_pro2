import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 该程序无法执行， 看 文末
def use_implicitly_baidu():
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.baidu.com/")

    search_elem = driver.find_element_by_id('index-kw')
    search_elem.send_keys("python")
    driver.implicitly_wait(10) # 10秒内完成所有操作， 相比time.sleep的优点是不用非得等待10秒，等待过程中只要操作完成就可以执行

    # 显示搜索结果条数
    if driver.find_element_by_class_name("nums").is_displayed():
        print(driver.find_element_by_class_name("nums").text)



# 改为使用bing搜索， 百度实在解决不了
# 然而使用bing之后搜索按钮也是隐藏的
def use_impplicitly_visit_bing():
    index_url = 'https://cn.bing.com/?FORM=Z9FD1'
    # 配置无界面
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=option)
    driver.get(index_url)

    # 搜索
    search_elem = driver.find_element_by_id("sb_form_q")
    search_btn = driver.find_element_by_class_name("form")
    search_btn.click()

    time.sleep(5)
    print(driver.page_source)


# 尝试跳过主页搜索，在子页面搜索， 使用百度。 测试成功
def visit_baidu_child():
    index_url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=cb4a407500000f04&rsv_t=a5c3hqbEA5EMTMO32yhu4vc2fm9%2BmEBp2ZpkFl2rilJAfC2PRsxcqtlbwxw&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&inputT=1351641&rsv_sug4=1351641'

    # 使用driver
    # 配置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)

    # 进行搜索
    search_elem = driver.find_element_by_id("kw")
    search_btn = driver.find_element_by_id("su")

    search_elem.clear()
    search_elem.send_keys("python")
    search_btn.click()

    time.sleep(5)
    print(driver.page_source)


if __name__ == '__main__':
    # use_implicitly_baidu()
    # use_impplicitly_visit_bing()
    visit_baidu_child()