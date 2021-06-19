from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_sum1 = browser.find_element_by_id("num1")
x_sum2 = browser.find_element_by_id("num2")
x1 = x_sum1.text
x2 = x_sum2.text
x = int(x1)+int(x2)
#print("x", x)

dropdown = Select(browser.find_element_by_id("dropdown"))
dropdown.select_by_value(str(x))

submit_button = browser.find_element_by_css_selector(".btn.btn-default")
submit_button.click()