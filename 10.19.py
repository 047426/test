
from selenium import webdriver
from datetime import time
class JD:
    def enter_correct(self):
        driver = webdriver.Chrome()
        driver.get('C:\\io\\jd_reg\\jd_reg\\jd_reg\\demo.html')
        time.sleep(2)
        driver.find_element_by_id('userName').send_keys('12346')
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('1111111')
        driver.find_element_by_xpath('//*[@id="pwd2"]').send_keys('1111111')
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('22445322')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys('18623454213')
        time.sleep(2)
        driver.find_element_by_css_selector("#ck").click()
        driver.find_element_by_id("btn").click()
    # 用户名输入为空
    def name_failed_null_info(self):
        driver = webdriver.Chrome()
        driver.get('C:\\io\\jd_reg\\jd_reg\\jd_reg\\demo.html')
        time.sleep(2)
        driver.find_element_by_css_selector("#ck").click()
        driver.find_element_by_id("btn").click()
    # 用户名输入正确
    def name_correct(self):
        driver = webdriver.Chrome()
        driver.get('C:\\io\\jd_reg\\jd_reg\\jd_reg\\demo.html')
        time.sleep(2)
        driver.find_element_by_id('userName').send_keys('12346')
        driver.find_element_by_id("btn").click()
     #用户名输入错误
    def name_error(self):
        driver = webdriver.Chrome()
        driver.get('C:\\io\\jd_reg\\jd_reg\\jd_reg\\demo.html')
        time.sleep(3)
        username_element = driver.find_element_by_id('username')
        driver.find_element_by_id("btn").click()
        print(username_element.get_attribute('placeholder'))
        if username_element.get_attribute('placeholder') == '格式错误，仅支持汉字、字母、数字、“-”“_”的组合':
            print('pass')
        else:
            print('failed')
    # 密码为错误
    def mima_null(self):
        driver = webdriver.Chrome()
        driver.get('C:\\io\\jd_reg\\jd_reg\\jd_reg\\demo.html')
        time.sleep(3)
        driver.find_element_by_id('username')
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('1111')
        driver.find_element_by_css_selector("#ck").click()
        driver.find_element_by_id("btn").click()

if __name__=='__mian__':
    jd=JD()
    jd.enter_correct()
    jd.name_failed_null_info()
    jd.name_correct()
    jd.mima_null()
    jd.name_error()

