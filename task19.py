# Using Exceptional handling to write Python Selenium codes

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TestCase1:
   #credintials
   username = "standard_user"
   password = "standard_user"

   #constructor
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def login(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(4)
           print(self.driver.title)
           print(self.driver.current_url)
           self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
           sleep(4)
           self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
           sleep(4)
           self.driver.find_element(by=By.XPATH, value='//*[@id="login-button"]').click()
           # Extract the entire page content
           page=self.driver.page_source
           with open("Webpage_task_11.txt", "w", encoding="utf-8") as text_file:
              text_file.write(page)
       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
           self.driver.quit()

url="https://www.saucedemo.com/"
TC = TestCase1(url)
TC.login()
