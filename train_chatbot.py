import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)


for intent in intents['intents']:
    for pattern in intent['patterns']:

        # tomar cada palabra y tokenizarla 
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # añadiendo mas tags
        documents.append((w, intent['tag']))

        # añadiendo mas clases
        if intent['tag'] not in classes:
            classes.append(intent['tag'])