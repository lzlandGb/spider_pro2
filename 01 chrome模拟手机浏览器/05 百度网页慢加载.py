import time


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def visit_baidu():
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.baidu.com/")
    # search_elem = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID, 'index-kw')))
    # print(search_elem)

    # use-agent
    User_Agent = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "BAIDUID=39B11E7613CDF6718B12E4F40712AC5A:FG=1; BIDUPSID=39B11E7613CDF6718B12E4F40712AC5A; PSTM=1530758645; MSA_PBT=146; MSA_ZOOM=1000; plus_lsv=6e7f7f82898256ea; plus_cv=1::m:d03af37f; MSA_WH=632_575; lsv=globalTjs_56c8eef-wwwTcss_fc2a91e-wwwBcss_0e614c8-sugjs_4686050-framejs_f97391f-globalBjs_2575c4b-wwwjs_cefd905; BD_HOME=0; H_PS_PSSID=1448_21080_26350_20927; BD_UPN=12314653; H_WISE_SIDS=124303_122155_124477_123800_123093_118629_120145_124267_124593_118888_118861_118846_118822_118797_107315_117328_117430_122789_124622_124070_123984_124559_124110_123813_124612_124525_123980_120260_124030_124298_110085_123289; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; Hm_lvt_12423ecbc0e2ca965d84259063d35238=1530840126,1530845477,1531101410; SE_LAUNCH=5%3A25518356; bd_traffictrace=090956_090958; BDSVRTM=339; Hm_lpvt_12423ecbc0e2ca965d84259063d35238=1531101481",
    }

    # time.sleep(10)
    # print(driver.page_source)

    print(dir(options.add_argument()))
    pass


if __name__ == '__main__':
    visit_baidu()