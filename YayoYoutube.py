from typing import KeysView
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:\\Users\\jkgmr13\\Desktop\\selenium practice\\chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path


driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
driver.implicitly_wait(5)

driver.get("https://www.youtube.com/watch?v=-lz5l5fG96I")
driver.find_element_by_xpath("//button[@aria-label='Play']").click()
driver.find_element_by_id("movie_player").send_keys('m')
driver.find_element_by_id("movie_player").send_keys(Keys.SHIFT+',')
driver.find_element_by_id("movie_player").send_keys(Keys.SHIFT+',')
driver.find_element_by_id("movie_player").send_keys(Keys.SHIFT+',')
driver.find_element_by_id("movie_player").send_keys(Keys.SHIFT+',')
time.sleep(2250)
driver.close()


    
