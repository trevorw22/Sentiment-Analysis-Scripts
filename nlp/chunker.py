import nltk
from nltk.tokenize import PunktSentenceTokenizer

class chunker:
	def chunker(self, text, pattern):
		custom_sent_tokenizer = PunktSentenceTokenizer(text)
		tokenized = custom_sent_tokenizer.tokenize(text)
		try:
			for i in tokenized:
				words = nltk.word_tokenize(i) # Split by word
				tagged = nltk.pos_tag(words) # Now pass through the NLP Part of Speech Tagging
				chunkGram = pattern 
				chunkParser = nltk.RegexpParser(chunkGram)
				chunked = chunkParser.parse(tagged)
				# chunked.draw()
				print(chunked)
		except Exception as e:
			print(str(e))