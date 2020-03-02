from time import sleep

from selenium import webdriver


class Basspage:
    _base_url = ""
    driver=None

    def __init__(self, driver: webdriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(3)
        else:
            self.driver = webdriver.Chrome()
            #
            # if self._base_url != "":
            #     self.driver.get(self._base_url)


