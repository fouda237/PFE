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
print("[ Running ] ")
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
log = driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# f = open("data1.txt")
# emails = f.read().split("\n")
# print(emails)
# f.close()
# print("[ Checking ] Emails")
# cp = 0
# for email in emails:
#     fb = open("emails_bounce.txt" , "a")
#     fv = open("emails_valide.txt" , "a")
#     try:
#         if len(email)<5:
#             continue

#         log = driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    
#         WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#identifierId')))
#         user=driver.find_element_by_id("identifierId")
#         #time.sleep(random.randint(1,2))
#         user.send_keys( email )
#         WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , "button[jscontroller='soHxf']")))
#         button=driver.find_element_by_css_selector("button[jscontroller='soHxf']")
#         button.click()
#         # check if good or not
#         try:
#             WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#pw_pwd')))
#             password_input = driver.find_element_by_css_selector("#pw_pwd")
#             print(True) 
#         except:
#             print(False)
#         res = check( email )
        
#         if( res ): 
#             fv.write( email + "\n")
#         else:
#             fb.write( email + "\n")

#         cp += 1
#         print(email+'>>'+str(cp))
#     except:
#             continue
#     fv.close()
#     fb.close()



  