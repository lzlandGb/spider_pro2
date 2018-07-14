import time
import re
import os


from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name="proxy.log")
# 设计存储对象
class Proxy():
    def __init__(self, ip=None, port=0, type=None, addr=None):
        self.ip = ip
        self.port = port
        self.type = type
        self.addr = addr


def create_driver(url):
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)

    return driver

# 获取所有page链接
def get_page_urls():
    url = "https://www.kuaidaili.com/free/inha/3/"
    driver = create_driver(url)

    driver.get(url)

    # 获取总页数
    res_count = ">(\d+)</a></li><li>页</li>"
    couont = int(re.findall(res_count, driver.page_source)[0])

    # 创建页面链接
    page_url_list = []
    for i in range(couont):
        page_url = "https://www.kuaidaili.com/free/inha/{0}/".format(i+1)
        page_url_list.append(page_url)

    # 检查
    # print(page_url_list)

    return page_url_list


# 捉取一页内容
def get_one_page_ips(url = "https://www.kuaidaili.com/free/inha/1/"):
    driver = create_driver(url)

    tr_elem_list = driver.find_elements_by_xpath("//tbody/tr")

    # 捉取ip
    proxy_list = []
    for tr_elem in tr_elem_list:
        tds = tr_elem.find_elements_by_tag_name('td')
        proxy = Proxy()
        proxy.ip = tds[0].text
        proxy.port = int(tds[1].text)
        proxy.type = tds[3].text
        proxy.addr = tds[4].text
        proxy_list.append(proxy)

    # 检查
    for proxy in proxy_list:
        print(proxy.ip)

    driver.quit()
    return proxy_list



if __name__ == '__main__':
    # get_one_page_ips()
    page_url_list = get_page_urls()
    i = 1
    for page_url in page_url_list:
        get_one_page_ips(page_url)
        logger.debug("第" + str(i) + "捉取完毕")
        i += 1