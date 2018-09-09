# Stop words are words without meaning that we want to pull out. ex: a, and, the...
# Sometimes people use sarcastic words as stop words
# This will save us alot of processing time especially for example if we are pulling articles from a database and need to process things
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

# Show us the default stop words that we set above
print(stop_words)

# Get the words into a list
words = word_tokenize(example_sentence)

# Create a new list for the filtered words
filtered_sentence = []

# Iterate through the list and add words if not in the filter list... This for loop has a one liner shown below
for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print(filtered_sentence)
# ['This', 'example', 'showing', 'stop', 'word', 'filtration', '.']



# One liner of the for loop and filtered_sentence list from above
# Word for word in words, if word isn't in stop_words, then its part of the filtered_sentence list we are making
filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)