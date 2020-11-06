from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))  # create dictionary with how many times item occurs
print(Counter(sentence.split()))  # count number of words in sentence

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])
print(dictionary['b'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)