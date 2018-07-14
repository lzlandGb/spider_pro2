import os
import time


from selenium import webdriver


from Tools.tools import debug_log


logger = debug_log(os.getcwd(), name='shucheng.log')


# 创建书本章节对象
class Book():
    def __init__(self, booke_num=0, book_name="未知"):
        self.booke_num = booke_num
        self.book_name = book_name
        self.capter_url_list = []
        self.capters = []


# 内容存储对象
# 章节对象
class Capter():
    def __init__(self, capter_num, capter_title, content):
        self.capter_num = capter_num # int
        self.capter_title = capter_title
        self.content = content


# 创建driver
def create_driver(url):
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)

    return driver


# 获取all capter 和 book num
def get_all_capter_urls(url = "http://www.51shucheng.net/kehuan/santi"):
    driver = create_driver(url)

    # 捉取all capter urls
    li_div_elems = driver.find_elements_by_class_name("mulu-list")
    book_num_div_elems = driver.find_elements_by_class_name("mulu-title")
    book_list = [] # 书本列表
    for i in range(len(book_num_div_elems)):
        # 获取书本序号
        book_name = book_num_div_elems[i].text
        booke_num = int(book_name.split("：")[0][-1])
        # 创建书本对象
        book = Book(booke_num=booke_num, book_name=book_name)
        # 获取章节elems
        book_capter_url_elems = li_div_elems[i].find_elements_by_tag_name('a')

        for book_one_url_elem in book_capter_url_elems:
            book.capter_url_list.append(book_one_url_elem.get_attribute("href"))
        book_list.append(book)

    return book_list

# 爬去一个篇章
def get_capter(url = "http://www.51shucheng.net/kehuan/santi/santi1/174.html"):

    driver = create_driver(url)

    # 获取章节标题
    time.sleep(4)
    capter_titile_elem = driver.find_elements_by_tag_name("h1")[0]
    capter_title = capter_titile_elem.text

    # debug
    # 解决最后一个后记章节无法解析的问题
    try:
        # 获取章节的序号
        capter_num = int(capter_title.split('.')[0])

    except ValueError:
        capter_num = 0

    # 获取章节内容
    content_elem = driver.find_element_by_class_name("neirong")
    content = content_elem.text

    capter = Capter(capter_num = capter_num, capter_title=capter_title, content=content)

    # 关闭浏览器
    driver.quit()

    return capter

    pass


if __name__ == '__main__':
    # capter = get_capter()
    book_list = get_all_capter_urls()
    for book_num in range(len(book_list)):
        for url in book_list[book_num].capter_url_list:
            logger.debug(url)
            capter_content = get_capter(url)
            book_list[book_num].capters.append(capter_content)
        logger.debug("第" + str(book_num + 1) + "本书完成")
        break

    # 检查结果
    for book_num in range(len(book_list)):
        print(book_list[book_num].book_name)
        for catper in book_list[book_num].capters:
            print(catper.capter_title)
            print(catper.content)

