from nltk.corpus import wordnet

class synsets:
	def synonym(self, text):
		synonyms = []

		for syn in  wordnet.synsets(text):
			for i in syn.lemmas():
				synonyms.append(i.name())
				# print("{0}\n{1}\n{2}\n{3}".format(i.name(), i.definition(), i.examples()))

		print(set(synonyms))
	def antonym(self, text):
		antonyms = []

		for syn in  wordnet.synsets(text):
			for i in syn.lemmas():
				if i.antonyms():
					antonyms.append(i.antonyms()[0].name())
					# print("{0}\n{1}\n{2}\n{3}".format(i.name(), i.definition(), i.examples()))
				# except Exception as e:
				# 	print("There were no antonyms.")
		print(set(antonyms))