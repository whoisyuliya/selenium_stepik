from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"
#link = "http://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1").text
    number2 = browser.find_element(By.ID, "num2").text
    
    answer = int(number1) + int(number2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))
 

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла