from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    link = " https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x))))) 

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)


    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()


finally:
    time.sleep(10)
    browser.quit()