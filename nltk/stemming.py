# Stemming is a form of preprocessing, we take the root word. ex. ridding is not rid (or rode)
# We can have several variations of words with the same meaning
# Word net is a newer program that can do the same thing as stemming but better

# The actual meaning of a word is unchanged because the root words are the same. See example below:
# I was taking a ride in the car.
# I was riding in the car.
# These mean the same thing, but the first one takes up alot more space in a database.
# Natural Language Processing has an algorithm that's been around since 1979 called the Porter Stemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for w in example_words:
# 	print(ps.stem(w))

# Output:
# python
# python
# python
# python
# pythonli

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
	print(ps.stem(w))