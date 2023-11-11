from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID,"num1").text
    num2 = browser.find_element(By.ID, "num2").text
    val = (int(num1) + int(num2))
    
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(str(val))

    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()