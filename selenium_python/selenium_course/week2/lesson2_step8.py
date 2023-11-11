from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/file_input.html"
    browser.get(link)


    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("PITR")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("PITROVICH")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("pitr@pitrovich.com")

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'donwload.txt') 
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
    