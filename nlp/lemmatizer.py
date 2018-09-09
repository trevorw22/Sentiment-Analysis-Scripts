from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class lemmatizer:
	def lemmatizer(self, text, type):
		tokenized = word_tokenize(text)
		lemmatizer = WordNetLemmatizer()		
		for i in tokenized:
			print("{0}/{1}".format(i, lemmatizer.lemmatize(i, pos=type)))