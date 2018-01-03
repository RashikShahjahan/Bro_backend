import nltk
import numpy
from nltk import Tree
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
tagged = nltk.pos_tag(clean_tokens)

#Puts words in categories
final = nltk.ne_chunk(tagged)

def fopen(tree):
    i = 0
    found = True
    open   = ''
    while found and i < len(str):
        if (tree[i]) == 'open':
            open  = tree[i+1]
            found = False
            return open
        else:
            i+=1

def fcall(tree):
    i = 0

    found  = True
    call   = ''

    while found and i < len(tree):
        if (tree[i][0]) == 'call':
            for subtree in tree.subtrees():
                if (subtree.label()) == 'PERSON':
                    call  = subtree[0][0]
                    found = False
                    return call



def fremind(tree):
    i = 0
    found   = True
    remind  = ''
    time    = ''
    while found and i < len(tree):
        if (tree[i]) == 'remind' or 'remember':

            for i in range(len(tree)-(i+1)):
                if tree[i+1][1]=='CD':
                    time = tree[i+1]

                else:
                    remind = remind + " " +(tree[i+1])



            found = False
            return remind
        else:
            i+=1

def ftext(tree):
    i = 0
    found = True
    text  = ''
    while found and i < len(tree):
        if (tree[i][0]) == 'text' or 'message' or 'tell':
            text = tree[i+1]
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

def fclose(str):
    i = 0
    found   = True
    close   = ''
    while found and i < len(str):
        if (str[i]) == 'close':
            close = str[i+1]
            found = False
            return close
        else:
            i+=1

def fclock(str):
    i = 0
    found   = True
    time    = False
    date    = False
    while found and i < len(str):
        if (str[i]) == 'time':
            time  = True
            found = False
            return time
        elif (str[i]) == 'date':
            date  = True
            found = False
            return date
        else:
            i+=1

def ftimer(str):
    i = 0
    found   = True
    while found and i < len(str):
        if (str[i]) == 'timer':
            timer = str[i-1]
            found = False
            return timer
        else:
            i+=1
