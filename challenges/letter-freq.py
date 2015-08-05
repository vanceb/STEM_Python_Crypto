import sys
import io

LETTERS = 'acbdefghijklmnopqrstuvwxyz'

def printSortedDict(dict, reverse=False):
    for key in sorted(dict, reverse=reverse):
        print(str(key) + ": " + str(dict[key]))

def invert(dict):
    inverted = {}
    for key in dict:
        if dict[key] in freq:
            inverted[dict[key]].append(key)
        else:
            inverted[dict[key]] = [key]
    return inverted

def frequency(dict, reverse=False):
    order = ''
    freq = invert(dict)
    for key in sorted(freq, reverse=reverse):
        for item in freq[key]: # allows for characters that occur exactly the same number of times
            order += item
    return order


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage: %s <filename> Where <filename> is the name of the file you want to process' % args[0])
        sys.exit(-1)
    else:
        freq = {}
        try:
            with io.open(args[1], mode='r', encoding='utf-8') as file:
                for line in file:
                    for character in line:
                        character = character.lower()
                        if character in LETTERS:
                            if character in freq:
                                freq[character] += 1
                            else:
                                freq[character] = 1
        except:
            print ('Problem reading file: %s' % args[1])


        print (frequency(freq))
