import os
import time


from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='login_taobao.log')

# 网页端无登陆按钮，直接抓取
def login_taobao():
    login_url = ""
    aim_url = ""
    # chrome无界面配置
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(login_url)

    print(driver.page_source)