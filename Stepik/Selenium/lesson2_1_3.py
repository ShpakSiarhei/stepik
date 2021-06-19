import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
browser.get(link)

x_element = browser.find_element_by_css_selector(".container  #input_value")
x = x_element.text
y = calc(x)

field1 = browser.find_element_by_id("answer")
field1.send_keys(y)

ch_box = browser.find_element_by_css_selector("[for='robotCheckbox']")
ch_box.click()

r_button = browser.find_element_by_css_selector("[for='robotsRule']")
r_button.click()

submit_button = browser.find_element_by_css_selector(".btn.btn-default")
submit_button.click()

