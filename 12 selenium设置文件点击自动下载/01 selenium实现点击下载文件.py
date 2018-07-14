import os
import time

from selenium import webdriver

from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name="dowload.log")

def dowload_file():
    index_url = "https://pypi.org/project/selenium/"
    current_dir = os.getcwd()
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # 配置下载文件点击下载   # 测试失败
    # prefs = {"profile.default_content_settings.popups":0, "download.default_directory": r"/workspace/sofeware/spider/pro2/12 selenium设置文件点击自动下载/"}
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': current_dir}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(index_url)


    # 进入下载页面
    download_elem = driver.find_element_by_id("files-tab")
    file_url = download_elem.get_attribute("href")
    driver.get(file_url)

    # 下载页面截图
    time.sleep(5)
    js = "window.scrollTo(200, 550);"
    driver.execute_script(js)
    driver.save_screenshot(os.getcwd() + "/dowload_page.png")

    # 点击下载
    file_elem = driver.find_element_by_partial_link_text("tar.gz")
    file_elem.click()


    time.sleep(10)
    driver.quit()
if __name__ == '__main__':
    dowload_file()