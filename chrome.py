# -*- coding: utf-8 -*-

"""
open browser
go to google.com
search for a <keyword>
parse first 10 results and save them
skip suggestions embedded videos
do it again on another browser
compare the results and print same results
#########################################
todo: reuse below program for firefox gecko browser 
todo: add Page Object Model
todo: refactor 
"""

import logging
from selenium.webdriver.common.keys import Keys
import string
from selenium import webdriver
#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service_obj = Service("/C:/Users/baris/AquaProjects/pythonselenium/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
action = ActionChains(driver)


driver.delete_all_cookies()
driver.get("https://www.google.com/")
driver.find_element(By.CSS_SELECTOR,"input[title='Ara']").send_keys("Araba",Keys.ENTER)
results = []
#headlines = driver.find_element(By.CSS_SELECTOR,"h3").get_attribute("normalize-space")
#headlines = driver.find_elements_by_link_text()
#driver.implicitly_wait(100)
#print(headlines)

title_elements = driver.find_elements(By.TAG_NAME,"h3")
title_texts = []
for label in title_elements:
    print(label.text)
    title_texts.append(label.text)
        
#with open('chromeData.csv','w',encoding='UTF8') as writer:
    #writer.writelines(title_texts)
         
with open('chromeData.csv','w',encoding='UTF8') as writer:
    for line in range(1,len(title_elements)):
        writer.write(title_texts[line]+'\n')

    writer.close()
     
    



            


    

        