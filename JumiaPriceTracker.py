#!/usr/bin/env python
# coding: utf-8

# #  App That Tracks Jumia Prices!
#  this program can track the specific pricemof an item from jumia

# In[1]:


import requests
from bs4 import BeautifulSoup
import smtplib
import time
import schedule


# In[2]:

def job():
    URL= 'https://www.jumia.co.ke/xiaomi-redmi-9a-6.53-2gb32gb-13.0mp-5000mah-4g-lte-dual-sim-grey-30887170.html'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


    # In[3]:


    page= requests.get(URL, headers= headers)

    soup= BeautifulSoup(page.content,'html.parser')


    # In[9]:


    # use class_ to get css class
    title= soup.find(class_="-fs20 -pts -pbxs").get_text()
    price= soup.find(class_="-b -ltr -tal -fs24").get_text()
    #convert price to float and removing the commma
    converted_price = float(price[4:].replace(',',''))
    #converted_price
    if converted_price< 10000.0:
        send_mail()
   



# In[5]:


#define fuctions to use to send mail
def send_mail():
    URL= 'https://www.jumia.co.ke/xiaomi-redmi-9a-6.53-2gb32gb-13.0mp-5000mah-4g-lte-dual-sim-grey-30887170.html'
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('joelnyagamuriithi@gmail.com', 'iqfpcreapyxjtulu')
    subject= 'Price Fell Down!'
    body= f'check the link {URL}'
    msg= f'Subject: {subject}\n\n{body}'
    server.sendmail(
        'joelnyagamuriithi@gmail.com',
        'nyagajoelmuriithi@gmail.com',
         msg
    )
    print('SENT MESSAGE')
    server.quit()

schedule.every(1).minutes.at(":00").do(job)
  

# In[8]:




# # Below is the program to find all class in a URL.(test program)
# from bs4 import BeautifulSoup
# import requests
#   
# ## Website URL
# URL = 'https://www.geeksforgeeks.org/'
#   
# ## class list set
# class_list = set()
#   
# ## Page content from Website URL
# page = requests.get( URL )
#   
# ## parse html content
# soup = BeautifulSoup( page.content , 'html.parser')
#   
# ## get all tags
# tags = {tag.name for tag in soup.find_all()}
# tags
# for tag in tags:
#   
#     # find all element of tag
#     for i in soup.find_all( tag ):
# ##         print(i.attrs)
#         # if tag has attribute of class
#         if i.has_attr( "class" ):
#   
#             if len( i['class'] ) != 0:
#                 class_list.add(" ".join( i['class']))
# class_list
#   
# 
