import nltk
from nltk.tokenize import PunktSentenceTokenizer


text = input("What would you like me to solve?\n")
sent_tokenized = PunktSentenceTokenizer(text)
tokenized = sent_tokenized.tokenize(text)

def processContent():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

	except Exception as e:
		print(str(e))

processContent()