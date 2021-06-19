import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)


field1 = browser.find_element_by_id("answer")
field1.send_keys(y)

ch_box = browser.find_element_by_id("robotCheckbox")
ch_box.click()

r_button = browser.find_element_by_id("robotsRule")
r_button.click()

submit_button = browser.find_element_by_css_selector(".btn.btn-default")
submit_button.click()

