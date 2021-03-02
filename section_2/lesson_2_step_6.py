from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	treasure = browser.find_element_by_id("input_value")
	x_element = treasure.text
	x = x_element
	y = calc(x)
	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)
	
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	
	check = browser.find_element_by_id("robotCheckbox")
	check.click()
	radio = browser.find_element_by_id("robotsRule")
	radio.click()
	#button = browser.find_element_by_css_selector(".btn.btn-default")
	button.click()


finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла