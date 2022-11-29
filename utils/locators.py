from selenium.webdriver.common.by import By




class MainPageLocators(object):
    LOGO = (By.CSS_SELECTOR, "img[alt='Google']")
    SEARCH_INPUT = (By.XPATH, '//input[@title="Search"]')
    SEARCH_BTN = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
    


class SearchPageLocators(object):
    TITLE = (By.TAG_NAME,"h3")
    
