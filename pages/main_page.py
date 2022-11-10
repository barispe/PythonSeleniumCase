from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Page objects
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH_INPUT).send_keys(item,Keys.ENTER)
        
    def get_headers(driver):
        title_elements = driver.find_elements(By.TAG_NAME,"h3")
        title_texts = []
        
        #Get texts of all the web elements
        for label in title_elements:
            print(label.text)
            title_texts.append(label.text)

        #write them to file        
        with open('chromeData.json','w',encoding='UTF8') as writer:

            for line in range(1,len(title_elements)):

                writer.write(title_texts[line]+'\n')

        writer.close()

    def setupFirefox():
        
        #service_obj = Service("/C:/Users/baris/AquaProjects/pythonselenium/drivers/geckodriver")
        webdriver.Firefox().get("https://www.google.com/")
        
        
        
        #options = Options()
        #driver = webdriver.Firefox()
        #options.add_argument("--headless") # Runs Chrome in headless mode.
        #options.add_argument('--no-sandbox')  # # Bypass OS security model
        #options.add_argument('disable-infobars')
        #options.add_argument("--disable-extensions")
        #options.add_argument("--start-fullscreen")
        #options.add_argument('--disable-gpu')
        #self.driver = webdriver.Firefox(options=options)
        #driver.get("https://www.google.com/")

            

        
    
            

    

        