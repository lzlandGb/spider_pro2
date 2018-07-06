import os


import selenium.webdriver
from selenium.webdriver.chrome.options import Options


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='chrome.log')
def use_chrome_withNonhead():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")  # root用户需加
    chrome_options.add_argument('--headless') # 无界面模式
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片

    driver = selenium.webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.cnblogs.com/z-x-y/p/9026226.html')

    print(driver.page_source)


if __name__ == '__main__':
    use_chrome_withNonhead()

