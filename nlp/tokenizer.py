from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize, word_tokenize
class tokenizer:
	def sentenceSplit(self, text):
		print(sent_tokenize(text))
	def wordSplit(self, text):
		print(word_tokenize(text))
	def punktSplit(self, text):
		tokenizer = PunktSentenceTokenizer()
		print(tokenizer.tokenize(text))