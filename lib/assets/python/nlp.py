#!/usr/bin/env python3

from textblob import TextBlob
print("ok")

text = open("transcript.txt")
print("ok")
b=text.read()
print(b)

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)


tokens = TextBlob(text)
print(tokens)
print(blob.tags) 
#tokens = nltk.word_tokenize(b)
tagged = nltk.pos_tag(tokens)
print(tokens)
#print(tagged)
with open('lib/assets/python/medical.txt') as file:
    medical_list = [i.strip() for i in file]



filtered = [t for t in tagged if t[1] == "NN" or t[1] == "JJ"]

new=[]
for i in range(len(filtered)):
    new.append(filtered[i][0])

final=[i for i in new if i in medical_list]
final=list(set(final))

for i in final:
    syns = wordnet.synsets(i)
    print(i+" : "+syns[0].definition()+"\n")
