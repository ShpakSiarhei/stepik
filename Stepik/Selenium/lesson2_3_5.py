import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn1st = browser.find_element_by_css_selector(".btn.btn-primary")
btn1st.click()

activetab = browser.window_handles[1]
browser.switch_to.window(activetab)
x_element = browser.find_element_by_css_selector(".container  #input_value")
x = x_element.text
y = calc(x)
print("y=:", y)

field1 = browser.find_element_by_id("answer")
field1.send_keys(y)

submit_button = browser.find_element_by_css_selector(".btn.btn-primary")
submit_button.click()