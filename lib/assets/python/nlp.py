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



text2=[]
for i in final:
	word = Word(i).definitions[0]
	text2.append(i)
	text2.append(": ")
	text2.append(word)
	text2.append("\n")
	text2.append("\n")

text_def=""
for i in text2:
	for j in i:

		text_def = text_def + j 
#text_def_final = text_def[12:]


text_def_final = text_def


with open("definitions.txt", "w") as myfile:
	myfile.write(text_def_final)


myfile.close()


text3 = open("language.txt")
l=text3.read()
lang=l.strip()


from googletrans import Translator



translator = Translator()

text4 = open("transcript.txt")
t4=text4.read()
tf4=t4.strip()

text5 = open("definitions.txt")
t5=text5.read()
tf5=t5.strip()

with open("translation.txt", "w") as myfile2:
	myfile2.write(tf4 + "\n" + tf5)
myfile2.close()


text6 = open("translation.txt")
t6=text6.read()
translations = translator.translate([t6], dest=lang)


text_def=""
for translation in translations:
    text_def+=translation.text

print(text_def)


with open("translation.txt", "w") as myfile3:
	myfile3.write(text_def)



myfile3.close()