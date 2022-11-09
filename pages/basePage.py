from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    def __init__(self, driver,base_url='https://www.google.com/'):
        self.driver = driver
        self.timeout = 30

    def find_element(self,*Locator):
        return self.driver.find_element(*Locator)

    def open(self,url):
        url == self.base_url
        self.driver.get(url)

    #Liste halinde donen elementler icin
    def find_elements(self,*Locator):
        return self.driver.find_elements(*Locator)
                            