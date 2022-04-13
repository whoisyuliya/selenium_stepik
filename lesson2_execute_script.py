from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    #Ввести данные в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    #scroll 
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    #Выбрать checkbox "I'm the robot".
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    #Переключить radiobutton "Robots rule!".
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()
    #Нажать на кнопку "Submit".
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла