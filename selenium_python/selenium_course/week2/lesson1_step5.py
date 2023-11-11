from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time



try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x))))) 

    element_X = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = element_X.text
    y = calc(x)

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()