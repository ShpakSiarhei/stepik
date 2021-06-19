import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/cats.html?"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_id("button") #Выскочит исключение