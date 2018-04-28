
# trying out google cloud natural lang api on comments scraped from amos yee vid (damn random LOL)

import time
import os
import pandas as pd
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import matplotlib.pyplot as plt
%matplotlib inline

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/vanessalam/Mydocuments/Mycodes/NLP/My Project-398df6a72b9c.json"

# read data
amos = pd.read_csv('amos.csv')

# Instantiate a client
client = language.LanguageServiceClient()



# get sentiment value (scale of -1 to 1) of ea comment

def get_sentiment(text):
    time.sleep(1)
    if type(text)!=str:
        text=""
    try:
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return sentiment.score
    except:
        return "check for error"

amos['sentiment'] = amos['textOriginal'].apply(get_sentiment)



# get length (no. of words) of each comment

def getlength(text):
    if type(text)!=str:
        return 0
    else:
        return len(text.split(" "))
amos['length'] = amos['textOriginal'].apply(getlength)



# make subset of data w/o errors and convert data type

clean = amos[amos.sentiment!="check for error"]
clean.sentiment = pd.to_numeric(clean.sentiment)


# view results

print('comment sentiment')
s_max = clean.sentiment.max()
s_min = clean.sentiment.min()
s_avg = clean.sentiment.mean()
s_med = clean.sentiment.median()
print("max: ", s_max,'\nmin: ', s_min, '\navg: ',s_avg,'\nmed: ',s_med)


print('comment length')
l_max = clean.length.max()
l_min = clean.length.min()
l_avg = round(clean.length.mean(),2)
l_med = clean.length.median()
print("max: ",l_max,"\nmin: ", l_min, '\navg: ',l_avg,'\nmed: ',l_med)


# distr on histogram

clean.sentiment.plot(kind="hist",bins=15)
clean.length.plot(kind="hist",bins=15)

