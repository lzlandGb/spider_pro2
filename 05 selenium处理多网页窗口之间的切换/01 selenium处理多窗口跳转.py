import time
import os
import re

from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='windows.log')
def handle_windowns():
    index_url = "https://baike.baidu.com/item/Java/85979?fr=aladdin"

    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)

    # 主窗口
    index_win = driver.current_window_handle

    # 进行登陆
    login_elem = driver.find_element_by_link_text("登录")
    login_elem.click()
    login_win = driver.current_window_handle
    time.sleep(3)

    # 给登陆界面截图
    driver.save_screenshot(os.getcwd() + '/登录.png')


    # 进行注册
    register_elem = driver.find_element_by_link_text("立即注册")
    register_elem.click()
    time.sleep(3)

    # 全部窗口
    allwins = driver.window_handles

    # 判断是否发生窗口跳转并且处理
    for win in allwins:
        if win != index_win:
            logger.debug("打开了新窗口")
            driver.switch_to.window(win)
            logger.debug("切换注册页面成功")
            user_elem = driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("simaxiaoliang0")
            password_elem = driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("l2l8tc..")
            phone_number_elem = driver.find_element_by_id("TANGRAM__PSP_3__phone").send_keys("17688166224")
            send_code_elem = driver.find_element_by_id("TANGRAM__PSP_3__verifyCodeSend").click()
            time.sleep(3)
            driver.save_screenshot(os.getcwd() + '/regist.png')

            # 如果手机号已经注册则返回主页
            res_registed = "该手机已注册"
            if re.findall(res_registed, driver.page_source):
                cancel_elem = driver.find_element_by_id("TANGRAM__PSP_23__confirm_cancel").click()

    time.sleep(3)
    driver.switch_to.window(index_win)
    time.sleep(3)
    driver.save_screenshot(os.getcwd() + '/back.png')
    driver.quit()
    pass


if __name__ == '__main__':
    handle_windowns()