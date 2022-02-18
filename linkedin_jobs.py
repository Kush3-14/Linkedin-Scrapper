'''
Program to scrape jobs in a specific field of linkedin using selenium

Author: Kumar Shivam

'''

import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('E:\Coding\Python Projects\WebScrapping\careerguide\careerguide\spiders\chromedriver.exe')
browser.get('https://www.linkedin.com/login')

username = browser.find_element_by_id('username')
username.send_keys('your username') # Replace it with your Username
password = browser.find_element_by_id('password')
password.send_keys('your password')# Replace it with your Password

login_button = browser.find_element_by_class_name('login__form_action_container ')
login_button.click()

# I am using Engineering as an example
browser.get('https://www.linkedin.com/jobs/search/?f_F=eng&geoId=111795395&location=Kolkata%2C%20West%20Bengal%2C%20India&sortBy=R')

scroll = 6 # Specify the number if times you want to scroll
job_names = []
for i in range(scroll):
    browser.find_element_by_tag_name("html").send_keys(Keys.SPACE)  # Scroll to the bottom of the page  
    jobs = browser.find_elements_by_class_name('full-width.artdeco-entity-lockup__title.ember-view')   
    for i in jobs:
        job_names.append(i.text)

scroll = 6
company = []
for i in range(scroll):
    browser.find_element_by_tag_name("html").send_keys(Keys.SPACE)
    comp = browser.find_elements_by_class_name("artdeco-entity-lockup__subtitle.ember-view")    
    for i in comp:
        company.append(i.text)

scroll = 6
location = []
for i in range(scroll):
    browser.find_element_by_tag_name("html").send_keys(Keys.SPACE)
    loc =  browser.find_elements_by_class_name("job-card-container__metadata-wrapper")    
    for i in loc:
        location.append(i.text)

# Creating a csv file to store all the data extracted
col = ["Job Position","Company","Location"]

df = pd.DataFrame({"Job Position":job_names,"Company":company,"Location":location})
df.to_csv("linkedin_jobs.csv")