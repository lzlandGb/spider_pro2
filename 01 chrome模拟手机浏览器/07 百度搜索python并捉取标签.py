import time


from selenium import webdriver


def use_baidu():
    index_url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=cb4a407500000f04&rsv_t=a5c3hqbEA5EMTMO32yhu4vc2fm9%2BmEBp2ZpkFl2rilJAfC2PRsxcqtlbwxw&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&inputT=1351641&rsv_sug4=1351641"

    # 设置无界面浏览器
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
    search_elem.send_keys("java")
    search_btn.click()

    # 获取数据
    time.sleep(5)
    data1_elems = driver.find_elements_by_xpath("//div[@class='result-op c-container xpath-log']/h3/a")
    data2_elems = driver.find_elements_by_xpath("//div[@class='result c-container ']/h3/a")

    for d in data1_elems:
        print(d.text + " " + d.get_attribute('href'))

    for d in data2_elems:
        print(d.text + " " + d.get_attribute('href'))




if __name__ == '__main__':
    use_baidu()