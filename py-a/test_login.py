from selenium.webdriver.common.by import By
from  selenium import webdriver

from page.index import Index


class Testlo:
    def setup(self):
        self.a1 = Index()

    def testlog(self):
        self.a1.go_link()

    def teardown(self):
        self.a1.clo()
