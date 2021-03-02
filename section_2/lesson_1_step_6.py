from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	people_radio = browser.find_element_by_id("peopleRule")
	people_checked = people_radio.get_attribute("checked")
	print("value of people radio: ", people_checked)
	assert people_checked == "true", "People radio is not selected by default "

	robots_radio = browser.find_element_by_id("robotsRule")
	robots_checked = robots_radio.get_attribute("checked")
	assert robots_checked is None
	
	button = browser.find_element_by_css_selector(".btn")
	button_disabled = button.get_attribute("disabled")
	print("value of button Submit: ", button_disabled)
	assert button_disabled is None

	time.sleep(12)
	button_disabled = button.get_attribute("disabled")
	print("value of button Submit after 10sec: ", button_disabled)
	assert button_disabled is not None


finally:
# успеваем скопировать код за 30 секунд
    #time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла