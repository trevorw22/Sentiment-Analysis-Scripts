from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class stopWords:
	def words(self, text):
		stop_words = set(stopwords.words("english"))
		words = word_tokenize(text)
		filtered_sentence = [w for w in words if not w in stop_words]
		print(filtered_sentence)