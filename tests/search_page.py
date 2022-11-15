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
from googlesearch import search
from bs4 import BeautifulSoup

class Main(BaseTest):

    def test_page_load(self):
        page = MainPage(self.driver)
        page.check_page_loaded()
        page.search_item("Computer")
        page.get_headers()
        MainPage.setupFirefox()
        
        #soup=BeautifulSoup(self.driver.page_source)
        #for link in soup.find_all('a'):
            #print(link.get('href',None),link.get_text())
        df1 = pd.read_csv("chromeData.csv", on_bad_lines='skip')
        df2 = pd.read_csv("firefoxData.csv", on_bad_lines='skip')

        #c_result = df1[df1.apply(tuple,1).isin(df2.apply(tuple,1))]
        #print(c_result)
        
        with open('same.csv', 'w') as outFile:
            for line in df1:
                if line in df2:
                    outFile.write(line)

        #with open('same.csv','w',encoding='UTF8') as writer:
            #for line in range(1,len(c_result)):
                #writer.write(c_result[line])


        

                


        
