import nltk
from nltk.tokenize import PunktSentenceTokenizer

class entityRecognition:
	def entityRecogniton(self, text, index):
		custom_sent_tokenizer = PunktSentenceTokenizer(text)
		tokenized = custom_sent_tokenizer.tokenize(text)
		try:
			for i in tokenized[index:]:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)
				namedEnt = nltk.ne_chunk(tagged, binary=False)
				namedEnt.draw()
				print(namedEnt)
				print(tagged)
		except Exception as e:
			print(str(e))