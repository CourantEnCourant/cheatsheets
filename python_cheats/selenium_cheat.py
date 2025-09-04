from typing import Optional

from selenium import webdriver

class Chrome(webdriver.Chrome):
    def __init__(self, service=None):
        """
        :param service: Takes in a Service() instance to download chrome webdriver automatically
        """
        super().__init__(service)

    def implicitly_wait(self, time_to_wait: float) -> None:
        """Tell webdriver to implicitly wait"""
        pass

    def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        """
        :param by: Takes in a By instance. By instance can be: ID, XPATH...
        :param value: The value passed to by argument
        :return:
        """
        pass

    def get(self, url):
        return """All elements of this url"""


from selenium.webdriver.common.by import By

class By(By):
    def __init__(self):
        self.ID = None
        self.XPATH = None
        self.CLASS_NAME = None
        self.CSS_SELECTOR = None
        'LINK_TEXT',
        'NAME',
        'PARTIAL_LINK_TEXT',
        'TAG_NAME',



from selenium.webdriver.remote.webelement import WebElement


class WebElement():
    def __init__(self):
        self.text = None

    def click(self):
        """Click on element"""
        pass
