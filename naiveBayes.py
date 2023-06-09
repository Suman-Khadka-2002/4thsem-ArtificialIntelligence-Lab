# -*- coding: utf-8 -*-
"""NaiveBayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TwNF3faB6o0LKckl7rLPHTWQ39DQLdzz
"""

#This program is used to detect if the email is spam (1) or not (0)

import numpy as np
# import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# from google.colab import files
# uploaded=files.upload()

df=pd.read_csv('spam_ham_dataset.csv')
df.head(5)

#print the shape (get the number of rows and columns)
df.shape

#get the column names
df.columns

#check for duplicates and remove them
df.drop_duplicates(inplace=True)

#no. of missing data (like NaN) for each column
df.isnull().sum()

#download the stopwords package
nltk.download('stopwords')

def process_text(text):
  nopunc=[char for char in text if char not in string.punctuation]
  nopunc=''.join(nopunc)

  clean_words=[word for word in nopunc.split() if word.lower() not in stopwords.words('english')] 

  return clean_words

#show the tokenization  (lemmas)
df['text'].head().apply(process_text)

#convert a collection of text to a matrix of tokens
from sklearn.feature_extraction.text import CountVectorizer
messages_bow=CountVectorizer(analyzer=process_text).fit_transform(df['text'])

#split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(messages_bow, df['label_num'], test_size=0.20, random_state=0)

#get the shape of messages_bow
messages_bow.shape

#create and train the Naive Bayes classifier
from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB().fit(X_train, y_train)

#print the predictions
print(classifier.predict(X_train))

#print the actual values
print(y_train.values)

#Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred=classifier.predict(X_train)
print(classification_report(y_train, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(y_train, pred))
print()
print('Accuracy: ', accuracy_score(y_train, pred))

#print the predictions
print(classifier.predict(X_test))

#print the actual values
print(y_test.values)

#Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred=classifier.predict(X_test)
print(classification_report(y_test, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(y_test, pred))
print()
print('Accuracy: ', accuracy_score(y_test, pred))
