from selenium import webdriver
from selenium.webdriver.common.by import By

from page.basepage import Basspage
from page.reg import Reg


class Index(Basspage):
    _base_url='https://work.weixin.qq.com'


    def go_link(self):
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()


    def clo(self):

        self.driver.quit()



