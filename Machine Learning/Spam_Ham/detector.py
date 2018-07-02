# source : https://www.youtube.com/watch?v=6Wd1C0-3RXM

import cPickle as c
import os
from sklearn import *
from collections import Counter

def load(clf_file):
	with open(clf_file) as fp:
		clf = c.load(fp)
	return clf

def make_dict():
	'''
	Extract all the words from all the emails and return a dictionary based on counts of each word.
	'''
	direc = "emails/"
	files = os.listdir(direc)

	emails = [direc + email for email in files]

	words=[]
	c = len(emails)

	for email in emails:
		f = open(email)
		blob = f.read()
		words += blob.split(' ')
		#print c
		c -= 1

	for i in range(len(words)):
		if not words[i].isalpha():
			words[i] = ""

	dictionary = Counter(words)
	del dictionary[""]
	return dictionary.most_common(3000)


clf = load("text-classifier.mdl")
d = make_dict()

while True:
	features = []
	input_text = raw_input(">").split()
	if input_text[0] == "exit":
		break
	for word in d:
		features.append(input_text.count(word[0]))

	result = clf.predict([features])
	print result
	print ["Not Spam","Spam"][result[0]]


