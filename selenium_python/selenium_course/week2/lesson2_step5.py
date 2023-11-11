from selenium import webdriver
from selenium.webdriver.common.by import By


# execute_script можно выполнить программу, написанную на языке JavaScript

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #делает скрол до кнопки внизу страницы
button.click()
