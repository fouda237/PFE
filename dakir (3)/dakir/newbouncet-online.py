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



def newFireFox( profil_number = "Not working :(" ):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    driver = webdriver.Firefox(capabilities=firefox_capabilities ) #, firefox_options=options)
    return driver


def check( email ):
    log = driver.get("https://accounts.login.idm.telekom.com/oauth2/auth?client_id=10LIVESAM30000004901PORTAL00000000000000&state=70404dc54d5112443aabc0a3cae6b4090d18ebe5906f0df6eb7d6dac3cc6844b&claims=%7B%22id_token%22%3A%7B%22urn%3Atelekom.com%3Aall%22%3Anull%7D%7D&nonce=70404dc54d5112443aabc0a3cae6b4090d18ebe5906f0df6eb7d6dac3cc6844b&redirect_uri=https%3A%2F%2Flogin.t-online.de%2Fcallback&logout_uri=https%3A%2F%2Flogin.t-online.de%2Ftelekom_logout&display=popup&scope=openid&response_type=code")
    
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#username')))
    user = driver.find_element_by_css_selector("#username")
    #time.sleep(random.randint(1,2))
    user.send_keys( email )
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#pw_submit')))
    a = driver.find_element_by_css_selector("#pw_submit")
    a.click()
    # check if good or not
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#pw_pwd')))
        password_input = driver.find_element_by_css_selector("#pw_pwd")
        return True
    except:
        return False
    
# main
print("[ Running ] ")
driver = webdriver.Chrome('chromedriver')
f = open("data1.txt")
emails = f.read().split("\n")
f.close()
print("[ Checking ] Emails")
cp = 0
for email in emails:
    fb = open("emails_bounce.txt" , "a")
    fv = open("emails_valide.txt" , "a")
    try:
        if len(email)<5:
            continue
        res = check( email )
        
        if( res ): fv.write( email + "\n")
        else:
            fb.write( email + "\n")

        cp += 1
        print(email+'>>'+str(cp))
    except:
            continue
    fv.close()
    fb.close()



