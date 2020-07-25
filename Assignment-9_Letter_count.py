'''
This code takes a sentence from the user,
counts the number of each letter of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.
'''
sentence = input('Please enter a sentence: ')

diction = {}

for i in sentence:
    keys = diction.keys()
    if i in keys:
        diction[i] += 1
    else:
        diction[i] = 1
print(diction)
