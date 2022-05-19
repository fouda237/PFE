from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/") 
print(driver.title)#Title  of the page 
driver.close #close the browser