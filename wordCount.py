__author__ = 'Arthur'
import operator
import json
import process
import string
import collections
from collections import Counter
from nltk.corpus import stopwords
import vincent

#Stop Words
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via','de','o']

with open('data/stream_twitterarthursun.json', 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in process.preprocess(tweet['text']) if term not in stop]
        #terms_hash = [term for term in process.preprocess(tweet['text'])
         #     if term.startswith('#')]
        #terms_single = set(terms_all)
        #terms_only = [term for term in process.preprocess(tweet['text'])
        #      if term not in stop and
        #      not term.startswith(('#', '@'))]
        #Update the counter
        count_all.update(terms_all)
        #count_all.update(terms_hash)
        #count_all.update(terms_only)
        #count_all.update(terms_single)





# Print the first 5 most frequent words
print(count_all.most_common(20))




'''
com = collections.defaultdict(lambda : collections.defaultdict(int))

# f is the file pointer to the JSON data set
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in process.preprocess(tweet['text'])
                  if term not in stop
                  and not term.startswith(('#', '@'))]

    # Build co-occurrence matrix
    for i in range(len(terms_only)-1):
        for j in range(i+1, len(terms_only)):
            w1, w2 = sorted([terms_only[i], terms_only[j]])
            if w1 != w2:
             com[w1][w2] += 1

com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = max(com[t1].items(), key=operator.itemgetter(1))[:5]
    for t2 in t1_max_terms:
        com_max.append(((t1, t2), com[t1][t2]))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])


##########################################################################
#Data Visualizaiton Part
word_freq = count_all.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')

'''
