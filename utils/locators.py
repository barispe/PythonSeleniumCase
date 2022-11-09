from selenium.webdriver.common.by import By




class MainPageLocators(object):
    LOGO = (By.CSS_SELECTOR, "img[alt='Google']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[title='Ara']")
    SEARCH_BTN = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
    


class SearchPageLocators(object):
    TITLE = (By.TAG_NAME,"h3")
    
