import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
%matplotlib inline

# read data

amos = pd.read_csv('amos.csv')
amos.info()


# find errors and remove columns

errors = []
for i in range(len(amos)):
    if type(amos.textOriginal[i])!=str:
        errors.append(i)

amos = amos.drop(errors)
comments = " ".join(amos.textOriginal)
comments = comments.lower()


# tokenize words

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokensraw = tokenizer.tokenize(comments)


# remove stopwords

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
tokens = [word for word in tokensraw if word not in stopwords]


# lemmatizer

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
# lemmatizer.lemmatize('text')


# stemmer

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
# stemmer.stem('text')


tokens_stem = [stemmer.stem(word) for word in tokens]
tokens_lem = [lemmatizer.lemmatize(word) for word in tokens]



# word cloud 1 - original

comments_wordcloud = WordCloud().generate(comments)
plt.figure(figsize=(12,8))
plt.imshow(comments_wordcloud)


# word cloud 2 - lemmatized

l_tokens = " ".join(tokens_lem)
tokens_wordcloud = WordCloud().generate(l_tokens)
plt.figure(figsize=(20,10))
plt.imshow(tokens_wordcloud)


