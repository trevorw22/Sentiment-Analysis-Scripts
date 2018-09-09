# First we want to know who or what the sentence is talking about, the named entity in the context, which is generally just a noun (a person, place or thing)
# Second step finding words that modify or affect that noun. We might have many named entities in the same sentence which is why we need chunking
# ex. Apple releases new iphone, and tesla announces home battery, but which one should I buy?
# Most people chunk into noun phrases, a noun or nouns with modifiers (descriptive words) around them. Kind of like a descriptive group of words surrounding that noun. 
# The downside to this is we can only use regex's, and only being able to group things as chunks and only create chunks of words that are touching each other
# To do the chunking, we use a mesh of the part of speech tags and regex's
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i) # Split by word
			tagged = nltk.pos_tag(words) # Now pass through the NLP Part of Speech Tagging

# We want any form of an adverb RB, and are looking for 0 or more of these, then do the same for a verb VB, then find one or more proper noun NNP(ex'Harrison') which is required, then a possible noun NN(ex'desk')
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""" # Chunk is an arbitrary name, we use <> to specify the Part of Speech(RB = Adverb)

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			chunked.draw()

			# print(chunked)

	except Exception as e:
		print(str(e))

process_content()