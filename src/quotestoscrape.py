import os
import platform

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class QuotesToScrape(object):
    """Selenium automation to scrape all quotes from Quotes to Scrape"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HOME = 'http://quotes.toscrape.com/'

    def __init__(self):
        """Keep the gecko driver in 'resources' by the name geckodriver"""

        driver_path = os.path.join(self.BASE_DIR, 'resources', 'geckodriver')
        if platform.system() == 'windows':
            driver_path += '.exe'
        self._driver = webdriver.Firefox(executable_path=driver_path)

    def __enter__(self):
        """."""

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """."""

        self._driver.quit()

    def _get_home(self):
        """Get the home page"""

        self._driver.get(self.HOME)

    def _retrieve_quotes(self):
        """Retrieve quotes by pagination"""

        quotes = self._driver.find_elements_by_class_name('quote')
        quotes_data = []
        for quote in quotes:
            quote_data = {
                'text': quote.find_element_by_class_name('text').text,
                'author': quote.find_element_by_class_name('author').text
            }
            quotes_data.append(quote_data)

        try:
            self._driver.find_element_by_class_name('next').find_element_by_tag_name('a').click()
            quotes_data.extend(self._retrieve_quotes())
        except NoSuchElementException:
            pass

        return quotes_data

    def parse(self):
        """Parse quotes"""

        self._get_home()
        quotes_data = self._retrieve_quotes()
        return quotes_data
