
# Save details of beauty and F&B related listings from MyFave for further cleaning/ analysis

import json, urllib, requests,re
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Create empty dataframe

listings=pd.DataFrame(columns=['Company Name','Company ID','Rating','Offer','Details','Original Price','Sale Price','percent_savings','Num_bought','Num_outlets','Outlet Names','Offer start date'])

# categories=['eat','beauty','activity','fitness','service','travel','staycation']
# preferences=['popularity','rating','price_low']

# Crawl first 100 pages of beauty-related listings arranged by popularity

n=1
for i in range(1,101):
	URL = ("https://myfave.com/singapore/beauty?&page="+str(i)+"&order=popularity")
	oururl= urllib.request.urlopen(URL).read()
	soup = BeautifulSoup(oururl,'html.parser')

	mytext=soup.find('script',text=re.compile("var OffersView"))

	searchresults=re.search('listings:(\d|\D)+filters:', str(mytext))
	jsontext=searchresults.group()

	jsontext=jsontext.replace("listings: ", "")
	jsontext=jsontext.replace("}],","}]")
	jsontext=jsontext.replace("filters:","")

	info = json.loads(jsontext)

	for item in info:
		company=item['company_name']
		company_id=item['company_id']
		rating=item['average_rating']
		description=item['name']
		details=item['description']
		original=item['original_price']
		sale=item['discounted_price']
		savings=item['discount']
		bought=item['purchases_count']
		outlet_no=item['outlets_count']
		outlet_name=item['outlet_names']
		started=item['start_date']
		listdetails=[company, company_id, rating, description, details,original, sale, savings, bought, outlet_no, outlet_name, started]
		listings.loc[n]= listdetails
		n+=1

listings['Date retrieved']=datetime.date.today()

listings.to_csv('listings_beauty.csv')

# Repeat for category=eat to get F&B listings into a separate listings_eat.csv file
# but F&B seems to have fewer listings only 30+ pages so there's probably more data to analyze for beauty-related listings)

# TO DO:
# item['url'] to access indiv listing page for more details, nlp on description/ comments

