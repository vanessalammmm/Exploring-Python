
# Exploring BeautifulSoup library w a web scraper to retrieve selected listings from MyFaves (previously Groupon)

import json, urllib, requests,re
from bs4 import BeautifulSoup

mycategory=str(input("Choose a category(eat/beauty/activity/fitness/service/travel/staycation): "))
mypref=str(input("Sort by popularity, rating or price_low? "))

URL = ("https://myfave.com/singapore/"+mycategory+"?order="+mypref)

oururl= urllib.request.urlopen(URL).read()
soup = BeautifulSoup(oururl,'html.parser')

mytext=soup.find('script',text=re.compile("var OffersView"))

searchresults=re.search('listings:(\d|\D)+filters:', str(mytext))
jsontext=searchresults.group()

jsontext=jsontext.replace("listings: ", "")
jsontext=jsontext.replace("}],","}]")
jsontext=jsontext.replace("filters:","")

info = json.loads(jsontext)
print('\n')
count=0
for item in info:
  if item['discount']>50:
    print('Company Name: '+ item['company_name'])
    print('Description: '+item['name'])
    print('Original price: '+item['original_price'])
    print('Now selling at: '+item['discounted_price'])
    print('Savings: '+ str(item['discount'])+'%')
    print(str(item['purchases_count'])+' people have bought!\n')
    count+=1
print('Offers retrieved: ',count)

