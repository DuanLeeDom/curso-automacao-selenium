import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = (Options)
main_directory = os.path.join(sys.path[0]) # 3
chrome_driver_path = ChromeDriverManager().install()

driver = webdriver.Chrome( executable_path=chrome_driver_path , chrome_options=chrome_options)

driver.get('https://www.selenium.dev/')