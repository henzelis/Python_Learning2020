#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import parameters # file with options: q_search_query = 'site:linkedin.com/in/ AND "Java Developer" AND "Ukraine"', file_name = 'results_file.csv', linkedin_username = 'e@mail.com', linkedin_password = 'YourPaSsWoRd'
import csv
from bs4 import BeautifulSoup
import re
import pickle

'''FUNCTION TO GET URLS FROM GOOGLE SEARCH PAGES'''

def get_linkedin_urls(regex_site):
    linkedin_urls = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        result = re.search(regex_site, elem.get_attribute("href"))
        if result:
            linkedin_urls.append(result.groups()[0])
    return linkedin_urls

''' NEED TO DOWNLOAD AND SET RIGHT LOCATION OF WEBDRIVER'''

driver = webdriver.Chrome('D:\Temp\chromedriver.exe')
driver.get('https://www.google.com')
search_query = driver.find_element_by_name('q') #find query by 'q' tag in html code
search_query.send_keys(parameters.q_search_query)
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb")) #optional step
search_query.send_keys(Keys.RETURN)

regex_site = r'(^https://ua.linkedin.com\S+)'
linkedin_urls = []

''' Go thue google search pages and get urls'''

while True:
    try:
        next_page = driver.find_element_by_id("pnnext")
        page_urls = get_linkedin_urls(regex_site)
        linkedin_urls.extend(page_urls)
        next_page.send_keys(Keys.RETURN)
        time.sleep(2)
    except:
        page_urls = get_linkedin_urls(regex_site)
        linkedin_urls.extend(page_urls)
        break

print(linkedin_urls)

'''Login to LINKEDIN'''

driver.get('https://www.linkedin.com')
time.sleep(3)
username = driver.find_element_by_name('session_key')
username.send_keys(parameters.linkedin_username)
password = driver.find_element_by_id('session_password')
password.send_keys(parameters.linkedin_password)
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
time.sleep(1)


''' Getting WEB SITE DATA '''

data_list = [['name', 'company', 'position', 'url']]

for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 768)") #Go down to load full page
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    try:
        name_src = soup.find('ul', {'class': 'pv-top-card--list'})
        name = re.search(r'\S+ \S+', name_src.text.lstrip()).group()
        experiance_src = soup.find('li', {'class': "pv-entity__position-group-pager"})
        experiance_list = re.split(r'[\n]+', experiance_src.text.strip())
        if "Company Name" in experiance_list[0]:
            company = experiance_list[1].strip()
            position = experiance_list[6].strip()
            print('Type 1', name, company, position)
        else:
            company = experiance_list[2].strip()
            position = experiance_list[0].strip()
            print('Type 2', name, company, position)
    except:
        print('Profile have no enough information to be explored')
        continue
    user = [name, company, position, linkedin_url]
    data_list.append(user)

driver.quit


with open('D:\linkedin_result.csv', 'w', newline='',  encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in data_list:
        print(row)
        writer.writerow(row)
        
