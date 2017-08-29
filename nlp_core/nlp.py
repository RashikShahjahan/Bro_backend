import nltk
import numpy
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet

sentence = input()

#Splits line into words
tokens = word_tokenize(sentence)

#Removes stop words
stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]

#Tags words with their respective parts of speech
#tagged = nltk.pos_tag(clean_tokens)

#Puts words in categories
#final = nltk.ne_chunk(tagged)

def fopen(str):
    i = 0
    found = True
    open   = ''
    while found and i < len(str):
        if (str[i]) == 'open':
            open  = str[i+1]
            found = False
            return open
        else:
            i+=1

def fcall(str):
    i = 0
    found  = True
    call   = ''
    while found and i < len(str):
        if (str[i]) == 'call':
            call  = str[i+1]
            found = False
            return call
        else:
            i+=1

def fremind(str):
    i = 0
    found   = True
    remind  = ''
    while found and i < len(str):
        if (str[i]) == 'remind' or 'remember':

            for i in range(len(str)-(i+1)):
                remind = remind + " " +(str[i+1])

            found = False
            return remind
        else:
            i+=1

def ftext(str):
    i = 0
    found = True
    text  = ''
    while found and i < len(str):
        if (str[i]) == 'text' or 'message' or 'tell':
            text = str[i+1]
            found = False
            return text
        else:
            i+=1

def fsearch(str):
    i = 0
    found  = True
    search = ''
    while found and i < len(str):
        if (str[i]) == 'search':
            found = False
            return search
        else:
            i+=1

print(fopen(clean_tokens))
print(fcall(clean_tokens))
print(fremind(clean_tokens))
