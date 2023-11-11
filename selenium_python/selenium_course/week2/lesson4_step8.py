from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = ("http://suninjuly.github.io/explicit_wait2.html")
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x))))) 


    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    number = browser.find_element(By.ID, "input_value").text
    y = calc(number)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
