from selenium import webdriver
from selenium.webdriver.common.by import By

import scrape_books.constants as const


class BookScraper(webdriver.Chrome):
    '''

    '''
    def __init__(self):
        super(BookScraper, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_price_of_book(self, book_name: str):
        xpath_str = "//a[contains(@title,'{}')]".format(book_name)
        self.find_element(By.XPATH, xpath_str).click()
        print(self.find_element(By.CSS_SELECTOR, 'p.price_color').text)



