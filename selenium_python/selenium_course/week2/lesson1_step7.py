from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time



try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x))))) 
    
    case_img = browser.find_element(By.ID, "treasure")
    case_val = case_img.get_attribute("valuex")
    x = case_val
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