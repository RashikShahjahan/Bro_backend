import nltk
import numpy
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet

open = False
call = False
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

if (final[0][0]) == 'open':
       open = True
       print (final[1][0])

elif (final[0][0]) == 'call':
         call = True
         print (final[1][0][0])
             
else:
    print ('error')


