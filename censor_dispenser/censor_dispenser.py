# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


"""censored = ["learning algorithms"]

def censorFromText(text):
	text_lowercase = text.lower()
	#print(text_lowercase)
	for phrase in censored:
		#print(phrase)
		if phrase in text_lowercase:
			#print(phrase)
			print(text.replace(phrase, "*" * len(phrase)))
	#print(text_split)

censorFromText(email_one)"""

censored = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

"""def censorFromText(text):
	#text_lowercase = text.lower()
	#print(text_lowercase)
	text_split = text.split()
	for phrase in censored:
		#Checking for censored phrases that are not a single word
		#if " " in phrase:
		phrase_split = phrase.split()
			#print(phrase_split)
		for word in range(len(text_split)):
				#print(word)
			if text_split[word].lower() == phrase_split[0]:
				match_count = []
				for p in range(len(phrase_split)):
					if phrase_split[p] in text_split[word + p].lower():
						match_count.append(text_split[word + p])
					#print(match_count)
				if range(len(match_count)) == range(len(phrase_split)):
						#print(match_count)
						#print(text_split[word].replace(text_split[word], "*" * len(text_split[word])))
					for i in range(len(match_count)):
							#print(i)
							#print(text_split[word + i])
						text_split[word + i] = "*" * len(text_split[word + i])

	print(" ".join(text_split))

#censorFromText(email_two) """

def censorFromText(text):
	text_split = text.split()
	neg_stored = []

	for word in text_split:
		#print(word)
		for letter in word:
			if letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
				word = word.replace(letter, "")
			#print(word)

	for word in range(len(text_split)):
		for neg in negative_words:
			if neg == text_split[word].lower():
				#print(text_split[word])
				neg_stored.append(text_split[word])
				if neg != neg_stored[0]:
					#print(text_split[word])
					text_split[word] = "*" * len(text_split[word])
					text_split[word - 1] = "*" * len(text_split[word - 1])
					text_split[word + 1] = "*" * len(text_split[word + 1])
					#print(text_split[word])
	#print(neg_stored)
	#print(len(neg_stored))
	#print(range(len(neg_stored)))

	for phrase in censored:
		#Checking for censored phrases that are not a single word
		#if " " in phrase:
		phrase_split = phrase.split()
			#print(phrase_split)
		for word in range(len(text_split)):
				#print(word)
			if text_split[word].lower() == phrase_split[0]:
				match_count = []
				for p in range(len(phrase_split)):
					if phrase_split[p] in text_split[word + p].lower():
						match_count.append(text_split[word + p])
					#print(match_count)
				if range(len(match_count)) == range(len(phrase_split)):
						#print(match_count)
						#print(text_split[word].replace(text_split[word], "*" * len(text_split[word])))
					for i in range(len(match_count)):
							#print(i)
							#print(text_split[word + i])
						text_split[word + i] = "*" * len(text_split[word + i])
						text_split[word + i - 1] = "*" * len(text_split[word + i - 1])
						text_split[word + i + 1] = "*" * len(text_split[word + i + 1])

	print(" ".join(text_split))

censorFromText(email_four)
