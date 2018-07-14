import os
import time


from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name="play_video.log")

def play_video():
    url = "http://videojs.com/"
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    # 点击视频播放
    # video_elem = driver.find_element_by_id("preview-player")
    video_emem = driver.find_element_by_class_name("vjs-big-play-button")
    video_emem.click()

    # 截图
    time.sleep(5)
    driver.save_screenshot(os.getcwd() + "/play_video.png")

    driver.quit()


if __name__ == '__main__':
    play_video()