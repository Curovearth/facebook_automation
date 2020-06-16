from selenium import webdriver
import time
from time import sleep
#you can use any other browser
driver = webdriver.Firefox()
driver.get('http://www.facebook.com')
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('your email-id for login')
time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('your password for login')
time.sleep(3)
login = driver.find_element_by_xpath('//*[@id="u_0_b"]')
time.sleep(4)
login.click()
#you are now into your facebook account
status = driver.find_element_by_xpath('//*[@id="js_5a"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div')
status.send_keys('Hi everyone.. Just playing with selenium')
statusbutton = driver.find_elements_by_tag_name('button')
time.sleep(3)
for button in buttons:
    if button.text == 'Post':
        button.click()

    