import pandas as pd
import numpy as np
import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

sw = stopwords.words('English')
lm = WordNetLemmatizer()

#read dataset

df = pd.read_csv('disaster_tweets_data.csv')

#checkiing for null values and duplicates

df.isnull().sum()
df.dropna()
df.drop_duplicates(inplace=True)

#after null and duplicate values are handled

print(df.shape)

# PRE PROCESSING DATASET

res = []
for i in df['tweets']:
    t = i.lower() #conveting into lowercase
    t = re.sub('[^A-Za-z0-9]',' ',t) #removing puntuations
    t = word_tokenize(t) #tokenizing words
    t = [i for i in t if i not in sw] #removing stop words
    t = [lm.lemmatize(i) for i in t] #lemmatizing
    t = " ".join(t) #joining tokenized words to sentences
    res.append(t) #adding these sentences into res (list)
print(res)

#selecting x and y variables

x = np.array(res)
y = df['target']
print(x.shape)
print(y.shape)

#splitting data into train and test

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#transforming tweets into vectorizer

cv = CountVectorizer(max_features=1200)
cv.fit(x_train)
x_train_cv = cv.transform(x_train)
x_test_cv = cv.transform(x_test)
print(x_train_cv.shape)
print(x_test_cv.shape)

#appling ML models

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

m1 = LogisticRegression()
m2 = MultinomialNB()
m3 = KNeighborsClassifier()

m1.fit(x_train_cv,y_train)
m2.fit(x_train_cv,y_train)
m3.fit(x_train_cv,y_train)

print('Train score of LogisticRegression =',m1.score(x_train_cv,y_train))
print('Test score of LogisticRegression =',m1.score(x_test_cv,y_test))
print('Train score of MultinomialNB =',m2.score(x_train_cv,y_train))
print('Test score of MultinomialNB =',m2.score(x_test_cv,y_test))
print('Train score of KNN model =',m3.score(x_train_cv,y_train))
print('Test score of KNN model =',m3.score(x_test_cv,y_test))

ypred_m1 = m1.predict(x_test_cv)
ypred_m2 = m2.predict(x_test_cv)
ypred_m3 = m3.predict(x_test_cv)

def eval_model(ytest,ypred):
    cm = confusion_matrix(ytest,ypred)
    print(cm)
    print(classification_report(ytest,ypred))

print('**************************LogisticRegression****************************')
eval_model(y_test,ypred_m1)
print('**************************Multinomial Naive Bayes****************************')
eval_model(y_test,ypred_m2)
print('**************************KNN Classification****************************')
eval_model(y_test,ypred_m3)

from sklearn.metrics import accuracy_score
LR = accuracy_score(y_test, ypred_m1)
NB = accuracy_score(y_test, ypred_m2)
KNN = accuracy_score(y_test, ypred_m3)

a = round(LR,2)
b = round(NB,2)
c = round(KNN,2)

if a > b and a > c:
	print('LogisticRegression has best accuracy')
elif b > a and b > c:
	print('Multinomial Naive Bayes has best accuracy')
else:
	print('KNN classification has best accuracy')

