#!/usr/bin/env python3

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from textblob import TextBlob


text = open("transcript.txt")
b=text.read()





tokens = TextBlob(b)
a= tokens.tags
with open('lib/assets/python/medical.txt') as file:
    medical_list = [i.strip() for i in file]



filtered = [t for t in a if t[1] == "NN" or t[1] == "JJ"]


new=[]
for i in range(len(filtered)):
    new.append(filtered[i][0])



final=[i for i in new if i in medical_list]
final=list(set(final))


from textblob import Word

print("ok")


text2=[]
for i in final:
	word = Word(i).definitions
	print(Word(i).definitions)
	text2.append(word)

print("ok")

with open("transcript.txt", "a") as myfile:
    myfile.write(text2)

    print("ok")
