# Author: NOURELDIN OSAMA
__author__ = "NOURELDIN OSAMA"
# Version : 1.4
__version__ = "1.0.4"

# Selenium for "Web Browser Automation"
from selenium import webdriver    # 3rd party packages

# Keys to "Scroll Down"
from selenium.webdriver.common.keys import Keys    # 3rd party packages

# to download the driver
from webdriver_manager.chrome import ChromeDriverManager    # 3rd party packages

# time to "Avoid ERRORS"
import time    # standard library

# to use mouse and keyboard
import pyautogui    # 3rd party packages


# Enter The Email To Sign in
Email = input("Enter Email: ")
# Enter The Password To Sign in
Password = input("Enter Password: ")

print("please don't use the device until the program finish")
time.sleep(3)

for i in range(5):
    print("The program starting in "+str(5-i)+" s")
    time.sleep(1)


# Start Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(1)
driver.maximize_window()



# go To Google Contacts and Sign in and Enter Email and Password
driver.get("https://contacts.google.com/directory")
enter_data1 = driver.find_element_by_name("identifier")
enter_data1.send_keys(Email)
click1 = driver.find_element_by_id("identifierNext")
click1.click()
time.sleep(4)

enter_data2 = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
enter_data2.send_keys(Password)
click2 = driver.find_element_by_id("passwordNext")
click2.click()
time.sleep(10)



# TO Zoom out to 25%  and press on the slider
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(1)
pyautogui.hotkey("ctrlleft", "-")
time.sleep(3)

pyautogui.moveTo(1908,190)
pyautogui.click()
time.sleep(2)



# we will use stop_element to break the infinite loop
stop_element = 'put the last element here'      # The Last Element in the page

Emails = []


while True:
    
    try:
        
        x = driver.find_elements_by_class_name("XXcuqd")
        Emails_page = [i.text for i in x]
        Emails += Emails_page

    except:
        print("Error")

    List_Emails = list(set(Emails))
    print(len(List_Emails))

    if stop_element in Emails:
        break
    
    # Scroll Down 1 page per time
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)           # wait until the page load

file = open("cc.txt","a")
file.writelines(List_Emails)
file.close()

file = open("cc2.txt","a")
file.writelines(Emails)
file.close()

print(List_Emails)
print(len(List_Emails))
print()
print(Emails)
print(len(Emails))
print()

file = open("cc.txt","a")
file.writelines(List_Emails)
file.close()

file = open("cc2.txt","a")
file.writelines(Emails)
file.close()

print("The script succeeded  '⚡🐍⚡🐲🐉⚡♥🔥☄♥'  ")

# 100% Accuracy





