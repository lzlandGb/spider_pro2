import  selenium.webdriver

def use_mobileemulation():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_experimental_option("mobileEmulation", {"deviceName":"iPhone 6 Plus"})

    driver = selenium.webdriver.Chrome(chrome_options=options)

    driver.get('http://www.baidu.com')

    print(driver.page_source)


if __name__ == '__main__':
    use_mobileemulation()
