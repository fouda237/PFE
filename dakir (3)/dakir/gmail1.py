from ast import Str
from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
# main
list_emails=[]

with open('C:/Users/fouda/OneDrive/Bureau/dakir (3)/dakir/100gmail.txt','r') as  email :
         for emails in email :
          list_emails.append(emails)
for ad_email in list_emails:
    str=ad_email.replace('\n',"")
    #driver = webdriver.Ie(executable_path="C:\Driver\IEDriverServer_Win32_4.0.0\IEDriverServer.exe")
    #driver=webdriver.Firefox(executable_path="C:\Driver\geckodriver_win64\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    log = driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#identifierId')))
    user=driver.find_element_by_id("identifierId")
    #time.sleep(random.randint(1,2))
    user.send_keys(str)
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , "button[jscontroller='soHxf']")))
    button=driver.find_element_by_css_selector("button[jscontroller='soHxf']")
    button.click()
    # time.sleep(5)

    # check if good or not
    try:
        # WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , "input[classe='F29zPe']")))
        # password_input = driver.find_element_by_css_selector("input[classe='F29zPe']")
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , "span[class='jibhHc']")))
        a=driver.find_element_by_css_selector("span[class='jibhHc']")
        print(False)
        fb = open("emails_bounce.txt" , "a")
        fb.write(str +'\n')
        fb.close()
    except:
        print(True) 
        fv = open("emails_valide.txt" , "a")
        fv.write(str +'\n')
        fv.close()
    driver.close()  

