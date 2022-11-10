import unittest
from tests.base_test import BaseTest
from pages.main_page import *
import logging
from selenium.webdriver.common.keys import Keys
import string
from selenium import webdriver
#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pages.base_page import BasePage
import pandas as pd

class Main(BaseTest):

    def test_page_load(self):
        page = MainPage(self.driver)
        page.check_page_loaded()
        page.search_item("Computer")
        page.get_headers()
        
        driverF = webdriver.Firefox()
        driverF.get("https://www.google.com/")
        driverF.find_element(By.CSS_SELECTOR, "input[title='Ara']").send_keys("Computer",Keys.ENTER)
        title_elements = driverF.find_elements(By.TAG_NAME,"h3")
        title_texts = []
        
        for label in title_elements:
            print(label.text)
            title_texts.append(label.text)
         
        with open('firefoxData.csv','w',encoding='UTF8') as writer:
            for line in range(1,len(title_elements)):
                writer.write(title_texts[line]+'\n')
        writer.close()        


        df1 = pd.read_csv("chromeData.csv")
        df2 = pd.read_csv("firefoxData.csv")

        c_result = df1[df1.apply(tuple,10).isin(df2.apply(tuple,10))]
        print(c_result)
        
        with open('same.csv','x',encoding='UTF8') as writer:
            for line in range(1,len(c_result)):
                writer.write(c_result[line])

                

