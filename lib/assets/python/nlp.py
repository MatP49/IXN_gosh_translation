#!/usr/bin/env python3

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from textblob import TextBlob
print("ok")

text = open("transcript.txt")
print("ok")
b=text.read()
print(b)


print("ok")



tokens = TextBlob(b)
a= tokens.tags
print(a)
#print(tagged)
with open('lib/assets/python/medical.txt') as file:
    medical_list = [i.strip() for i in file]



filtered = [t for t in a if t[1] == "NN" or t[1] == "JJ"]

print(filtered)

new=[]
for i in range(len(filtered)):
    new.append(filtered[i][0])


print(new)

final=[i for i in new if i in medical_list]
final=list(set(final))

print(final) 

from textblob import Word



for i in final:
	word = Word(i)
    defr = Word("octopus").definitions
    print(i+": "+ defr + "\n")
