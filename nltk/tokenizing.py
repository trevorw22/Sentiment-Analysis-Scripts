# import nltk
# nltk.download()

# tokenizing - word tokenizer (separates by words), sentence tokenizers (separates by sentence)

# lexicon and corporas

# corpora - body of text. ex: medical journals, presidential speeches, English language

# lexicon - words and their meanings
# investor-speak... regular english-speak
# investor speak 'bull' = someone who is positive about the market
# english-speak 'bull' = scary animal you don't want running @ you


from nltk.tokenize import sent_tokenize, word_tokenize

# How can we split this up in a list? We could use regex, but it would have to be very complex to separate things like Mr. 
example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."
# How do we split up sentences and separate words?
# print(sent_tokenize(example_text))
# print(word_tokenize(example_text)) # By default it leaves the period in Mr. with Mr when splitting it up in the list

for i in word_tokenize(example_text):
	print(i)
