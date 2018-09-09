from nltk import word_tokenize, pos_tag
from nltk.tokenize import PunktSentenceTokenizer

class partSpeech:

	def partSpeech(self, text):
		custom_sent_tokenizer = PunktSentenceTokenizer(text)

		tokenized = custom_sent_tokenizer.tokenize(text)
		try:
			for i in tokenized:
				words = word_tokenize(i) # Split by word
				tagged = pos_tag(words) # Now pass through the NLP Part of Speech Tagging

				print(tagged)

		except Exception as e:
			print(str(e))