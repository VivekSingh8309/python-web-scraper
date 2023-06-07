#!/usr/bin/env python
# coding: utf-8

# In[73]:


pip install requests


# In[74]:


pip install beautifulSoup4


# In[75]:


pip install lxml


# In[76]:


from bs4 import BeautifulSoup
import requests


# In[89]:


html_text = requests.get('https://m.timesjobs.com/jobs-by-roles/software-programmer-jobs').text
print(html_text)


# In[90]:


soup = BeautifulSoup(html_text,'lxml')
soup


# In[187]:


jobs = soup.find_all('div',class_= 'srp-job-bx')
for job in jobs:
    company_name = job.find('h4').text
    skill = job.find('div', class_='srp-keyskills').text
    more_info = job.find('h3').a['href']
    published_date = job.find('span', class_='posting-time').text
    print(f"Company Name: {company_name.strip()}")
    print(f"Skills Required: {skill.strip()}")
    print(more_info.strip())
    print(f"Job Posted: {published_date.strip()}")
    
    print('')


# In[ ]:




