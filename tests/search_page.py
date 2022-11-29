
from tests.base_test import BaseTest
from pages.main_page import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pages.base_page import BasePage
import pandas as pd
from googlesearch import search

class Main(BaseTest):
    #Program to scrape google results and write to chromeData.csv
    def test_page_load(self):
        page = MainPage(self.driver)
        page.check_page_loaded()
        page.search_item("Computer")
        page.get_headers()
    #Above program to run on firefox     
        MainPage.setupFirefox()
        df1 = pd.read_csv("chromeData.csv", on_bad_lines='skip')
        df2 = pd.read_csv("firefoxData.csv", on_bad_lines='skip')
        
        with open('same.csv', 'w') as outFile:
            for line in df1:
                if line in df2:
                    outFile.write(line)



        

                


        
