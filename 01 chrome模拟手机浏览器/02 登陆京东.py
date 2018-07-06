import os
import re
import time


from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='login_jd.log')
# 未成功， 元素没有加载
def login_jd():
    login_url = "https://plogin.m.jd.com/user/login.action?appid=100&kpkey=&returnurl=http%3A%2F%2Fhome.m.jd.com%2FmyJd%2Fhome.action%3Fsid%3D583ee9874b9874ddf1515a4ada050e44"
    aim_url = ""
    # 无界面设置
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(login_url)

    # 登陆
    username_elem = driver.find_element_by_id("username")
    password_elem = driver.find_element_by_id("password")
    login_elem = driver.find_element_by_id("loginBtn")

    time.sleep(4)
    username_elem.send_keys('17688166224')
    password_elem.send_keys("l2l8tc..")
    login_elem.click()

    # 判断是否登陆成功
    time.sleep(5)
    restr_my_jd = '账号管理'
    my_jd = re.findall(restr_my_jd, driver.page_source)
    print(my_jd)

    if not my_jd:
        # 解决历史收货人验证
        restr_history_people = "历史收货人"
        if_history_people = re.findall(restr_history_people, driver.page_source)
        if if_history_people:
            logger.debug("需要填写历史收货人")
            time.sleep(5)
            driver.save_screenshot(os.getcwd() + '/login_jd.png')
            # verify_input_elem = driver.find_element_by_class_name("verify-input")
            print(driver.page_source)



if __name__ == '__main__':
    login_jd()