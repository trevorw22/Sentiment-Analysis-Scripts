from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class stemming:
	def stemmer(self, text):
		ps = PorterStemmer()
		words = word_tokenize(text)
		for w in words:
			print(ps.stem(w))