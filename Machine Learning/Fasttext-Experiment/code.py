##############################################
#
#source: https://pypi.org/project/fasttext/
#
##############################################

import fasttext

classifier = fasttext.supervised('train_data.txt', 'model',label_prefix='__label__')
result = classifier.test('test_data.txt')
print 'P@1:', result.precision
print 'R@1:', result.recall
print 'Number of examples:', result.nexamples

texts = ['example very long text 1', 'example very longtext 2']
labels = classifier.predict(texts)
print labels

# Or with the probability
labels = classifier.predict_proba(texts)
print labels


# with k value  to get the k-best labels from classifier:
labels = classifier.predict(texts, k=3)
print labels

# Or with the probability
labels = classifier.predict_proba(texts, k=3)
print labels
