import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
firstname.send_keys("Name")

lastname = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
lastname.send_keys("Lastname")

email = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
email.send_keys("email@email.com")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element = browser.find_element_by_name("file")
print(file_path)
element.send_keys(file_path)
#print(os.path.abspath(__file__))
#print(os.path.abspath(os.path.dirname(__file__)))
#element.send_keys(file_path)
#attach_file = browser.find_element_by_xpath("/html/body/div/form/input")
#element = browser.find_element_by_css_selector("input#file")
#attach_click = attach_file.get_attribute("file")
submit_button = browser.find_element_by_css_selector(".btn")
submit_button.click()