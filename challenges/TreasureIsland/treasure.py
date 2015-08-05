
import io
import re

UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def add(wordlist):
    for word in wordlist:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

def spaceTokenize(line):
    return line.split()

def doubleDashTokenize(line):
    wordlist = []
    if len(line) > 0:
        for word in line:
            for token in word.split("--"):
                wordlist.append(token)
    return wordlist


def stripPunctuation(line):
    wordlist = []
    if len(line) > 0:
        for word in line:
            wordlist.append(re.split("[\'\"!;:,\.\?]", word)[0])
    return wordlist

def filterNames(line):
    wordlist = []
    for word in line:
        if len(word) > 0:
            if word[0] in UPPERCASE:
                wordlist.append(word)
    return wordlist

def freqs(words):
    freq = {}
    for word in words:
        if words[word] in freq:
            freq[words[word]].append(word)
        else:
            freq[words[word]] = [word]
    return freq

def printSortedDict(dict):
    for key in sorted(dict):
        print str(key) + ": " + str(dict[key])

words = {}
with io.open('Alice.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        add(filterNames(stripPunctuation(doubleDashTokenize(spaceTokenize(line)))))

printSortedDict(freqs(words))
