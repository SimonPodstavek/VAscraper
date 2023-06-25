import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


os.environ['PATH'] = r'C:\Users\Admin\Desktop\chromedriver_win32'

options = webdriver.ChromeOptions()
preferences = {'download.default_directory' : r'C:\Users\Admin\Desktop\va\temp'}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.virtual-academy.sk/portal/') 
driver.add_cookie({'name': 'MoodleSession', 'value': '3d038c081154262021718c138e4b7525'})
driver.refresh()

temp = []

for i in range(2,3):
    driver.get(f'https://www.virtual-academy.sk/portal/course/view.php?id={i}')
    temp = driver.find_elements_by_xpath('//ul[@class="breadcrumb"]/li/span[1]/a/span')
    folders = [folder.text for folder in temp]
    folders = '/'.join(folders)
    print(folders)
    driver.find_element(By.XPATH, '//div[@class="activityinstance"]/a').click()
    # os.replace()
    



