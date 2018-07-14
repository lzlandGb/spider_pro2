import os
import time

from selenium import webdriver
import selenium.common

from Tools.tools import debug_log

logger = debug_log(os.getcwd(), name="play_tengxun.log")


def play_tengxun_video():
    index_url = "https://v.qq.com/"
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)

    # debug timeout的情况下再试一次
    n = 1
    while n < 3:
        try:
            driver.get(index_url)

            # 当前窗口
            index_win = driver.current_window_handle

            # 进入动漫频道
            commic_elem = driver.find_element_by_link_text("动漫")
            commic_elem.click()
            allwins = driver.window_handles
            for win in allwins:
                if win != index_win:
                    print("窗口发生跳转")
                    driver.switch_to.window(win)

                    # 点击播放第一步动漫
                    vip_movie_div_elem = driver.find_element_by_id("v_cartoon_v3_vip")
                    vip_movie_elems = vip_movie_div_elem.find_elements_by_tag_name("li")
                    vip_movie_elems[0].click()

                    # 跳转到播放页面
                    commic_index_win = driver.current_window_handle
                    allwins = driver.window_handles
                    for win in allwins:
                        if win != index_win and win != commic_index_win:
                            print("又跳转了")
                            # 动漫播放的窗口
                            commic_playing_win = win
                            driver.switch_to.window(win)

                            # 给播放窗口截图
                            time.sleep(10)
                            driver.save_screenshot(os.getcwd() + "/playing2.png")


            driver.quit()
        except selenium.common.exceptions.TimeoutException:
            if n > 3:
                logger.debug("访问超时正在从新尝试")
            if n == 2:
                logger.debug("这是最后的尝试")
            n += 1
        else:
            logger.debug("截图成功")
            break


if __name__ == '__main__':
    play_tengxun_video()