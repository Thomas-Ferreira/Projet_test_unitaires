import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pandas as pd
from pprint import pprint
from pymongo import MongoClient

chromeOptions = webdriver.ChromeOptions()
s = Service(r'C:/Users/thoma/OneDrive/Bureau/chrome-driver/chromedriver.exe')
browser = webdriver.Chrome(service=s)

browser.get('https://www.zalando.fr/')
time.sleep(3)

cookies = browser.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
cookies.click()
time.sleep(2)

homme = browser.find_element_by_xpath('//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/nav/ul/li[2]/a')
homme.click()
time.sleep(1)

chaussures = browser.find_element_by_xpath('//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/nav/ul/li[3]/span/a',)
chaussures.click()
time.sleep(2)

sneakers = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[7]/div/div[1]/div/ul/li/ul/li[1]/a/span")
sneakers.click()
time.sleep(2)

li_marque = []
li_titre = []
li_prix = []

for i in range (0,4):
    articles = browser.find_elements_by_tag_name('article')
    articles[i].click()

    marque = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[2]/x-wrapper-re-1-4/div/div/a/span/h3")
    #print(item.text)

    titre = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[2]/x-wrapper-re-1-4/div/h1/span")
    #print(marque.text)

    prix = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[2]/x-wrapper-re-1-4/div/div/div/div/span")
    #print(prix.text)
    
    li_marque.append(marque.text)
    li_titre.append(titre.text)
    li_prix.append(prix.text)

    browser.back()
    time.sleep(2)
    
dictionary = {"marque": li_marque, "titre": li_titre,"prix":li_prix}
df = pd.DataFrame(dictionary)
    
#pprint(df) 

browser.close() # fermer le navigateur

client = MongoClient("mongodb+srv://user1:root@cluster0.iw7et.mongodb.net/ProjetTestUnitaires?retryWrites=true&w=majority")
collection = client.ProjetTestUnitaires
db = collection.TestUnit

#print(db)
#dict_js = df.to_json()
#print(dict_js)

db.insert_many(df.to_dict('records'))