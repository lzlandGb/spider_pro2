import re
import os

from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='04 dowload_meinv.log')
def create_driver(url=None):
    # 设置无界面模式
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)
    return driver

# all_page_urls
# def get_all_page_urls():
#     url = 'http://m.umei.cc/p/gaoqing/rihan/1.htm'
#     # url = 'http://m.umei.cc/p/gaoqing/rihan/'
#     driver = create_driver(url)
#
#     res_page_num = "<strong id='pagelist_all'>(\d+)</strong>"
#     page_num = re.findall(res_page_num, driver.page_source)
#
#     driver.quit()
#     print(page_num)
def get_all_page_urls():
    import urllib.request
    url = 'http://m.umei.cc/p/gaoqing/rihan/1.htm'
    response = urllib.request.urlopen(url)

    page_source = response.read().decode("utf-8")

    # 获取总页数
    res_page_num = "<strong id='pagelist_all'>(\d+)</strong>"
    page_num = int(re.findall(res_page_num, page_source)[0])

    page_url_list = []
    new_url = 'http://m.umei.cc/p/gaoqing/rihan/page_num.htm'
    for i in range(page_num + 1):
        u = new_url.replace("page_num", str(i+1))
        page_url_list.append(u)

    return  page_url_list


# one_page_persons
def get_one_page_persons(url=None):
    driver = create_driver(url)

    time.sleep(5)
    one_page_xpath = '//div/ul/li/a'
    person_elems = driver.find_elements_by_xpath(one_page_xpath)
    person_url_list = []
    for e in person_elems:
        person_url_list.append(e.get_attribute("href"))

    driver.quit()
    return person_url_list


# person_urls person_name
def get_person_urls(url = "http://m.umei.cc/p/gaoqing/rihan/78311.htm"):

    driver = create_driver(url)

    # person_name
    time.sleep(5)
    res_name = '<title>(.*)</title>'
    person_name = re.findall(res_name, driver.page_source)[0]


    # 爬取全部图片链接
    # 获取总页数
    res_page_all = '<a id="page_all">(\d+)</a>'
    page_all = int(re.findall(res_page_all, driver.page_source)[0])
    # 获取链接
    p_urls = []
    p_urls.append(url)
    # 设置url
    new_url = url.split('.')
    new_url[-2] =  new_url[-2] + '_' + "page_num"
    new_url = ".".join(new_url)

    # 获取urls
    for i in range(page_all-1):
        n_url = new_url.replace("page_num", str(i+2))
        p_urls.append(n_url)

    driver.quit()
    return p_urls, person_name


# 下载一张照片
def get_one_picture(url=None, dirname = 'canglaoshi'):
    import urllib.request

    driver = create_driver(url)

    # 获取图片
    img_xpath = "//div[@id = 'ArticleBox']/p/img"
    picture_elem = driver.find_element_by_xpath(img_xpath)

    # 照片名字
    picture_name = picture_elem.get_attribute("alt")
    try:
        # 创建文件夹
        os.mkdir(os.getcwd() + "/" + dirname)
    except FileExistsError:
        pass

    # 下载照片
    time.sleep(5)
    download_url = picture_elem.get_attribute("src")

    urllib.request.urlretrieve(download_url,dirname + '/' + picture_name + 'test.jpg')
    time.sleep(5)

if __name__ == '__main__':
    import time
    # 创建图片对象
    class Picture():
        def __init__(self, name, dirname):
            self.name = name
            self.dirname = dirname

    # 设置图像对象李彪
    picture_obj_list = []

    # 获取所有网页链接
    page_url_list = get_all_page_urls()
    for page_url in page_url_list:
        # 获取一张网页中所有的美女链接
        one_page_person_urls = get_one_page_persons(page_url)
        for person_urls in one_page_person_urls:
            # 下载每位美女
            person_info_urls = get_person_urls(person_urls)
            print(person_info_urls)
            for img_url in person_info_urls[0]:
                # 将图片设置成picture对象
                picture = Picture(img_url, person_info_urls[1])
                picture_obj_list.append(picture)

            logger.debug("第一位美女下载完成")
            break
        break

    for picture_obj in picture_obj_list:
        print(picture_obj.name)
        get_one_picture(picture_obj.name, picture_obj.dirname)