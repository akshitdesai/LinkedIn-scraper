#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install beautifulsoup4')


# In[60]:


import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup


# In[61]:


browser = webdriver.Chrome('driver/chromedriver.exe')


# In[62]:


browser.get('https://www.linkedin.com/uas/login')


# In[63]:


file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


# In[64]:


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)


# In[65]:


elementID = browser.find_element_by_id('password')
elementID.send_keys(password)


# In[66]:


elementID.submit()


# In[40]:


def replaceSpaces(string): 
      
    # Remove remove leading and trailing spaces 
    string = string.strip() 
  
    i = len(string) 
  
    # count spaces and find current length 
    space_count = string.count(' ') 
  
    # Find new length. 
    new_length = i + space_count * 2
  
    # New length must be smaller than length 
    # of string provided. 
    if new_length > 1000: 
        return -1
  
    # Start filling character from end 
    index = new_length - 1
  
    string = list(string) 
  
    # Fill string array 
    for f in range(i - 2, new_length - 2): 
        string.append('0') 
  
    # Fill rest of the string from end 
    for j in range(i - 1, 0, -1): 
  
        # inserts %20 in place of space 
        if string[j] == ' ': 
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else: 
            string[index] = string[j] 
            index -= 1
  
    return ''.join(string) 


# In[84]:


comp_name = replaceSpaces("Axis Bank Ltd.")
print(comp_name)


# In[85]:


browser.get('https://www.linkedin.com/search/results/companies/?keywords='+comp_name)


# In[86]:


soup = BeautifulSoup(browser.page_source)


# In[87]:


def getCompanyLink(soup):

    pav = soup.find('ul',{'class':'search-results__list list-style-none'})
    links = pav.findAll('a',{'class':'search-result__result-link ember-view'})

    company_link = 'https://www.linkedin.com'+links[0].get('href')
    return company_link


# In[163]:


def getprofiles(soup):
    
    pav = soup.find('ul',{'class':'org-people-profiles-module__profile-list'})
    links = pav.findAll('a',{'class':'link-without-visited-state ember-view'})
    list_CEO = []
    i= 1
    for link in links:
        user_link = link.get('href')
        i += 1
        list_CEO.append(user_link)
        if(i>=5):
            break
    return list_CEO


# In[89]:


company_link = getCompanyLink(soup)


# In[146]:


#For CEO Search
browser.get(company_link+'/people/?keywords=CEO')


# In[164]:


#For CEO url list
comp_prof = []
soup = BeautifulSoup(browser.page_source)
comp_prof = getprofiles(soup)
print(comp_prof)


# In[58]:


#For Marketing Manager

browser.get(company_link+'/people/?keywords=manager')


# In[ ]:



    

