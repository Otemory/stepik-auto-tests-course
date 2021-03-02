from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



link = "http://suninjuly.github.io/selects2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	num1 = browser.find_element_by_id("num1")
	x = num1.text
	num2 = browser.find_element_by_id("num2")
	y = num2.text
	answer = int(x) + int(y)
	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_value(str(answer))
	#сложный вариант
	#browser.find_element_by_tag_name("select").click()
	#browser.find_element_by_css_selector("[value='" + str(answer) + "']").click()
	
	
	button = browser.find_element_by_css_selector(".btn.btn-default")
	button.click()


finally:
# успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла