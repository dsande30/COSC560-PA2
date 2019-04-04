#!/usr/bin/env python3

import sys
from operator import itemgetter

if len(sys.argv) != 2:
    print("1 input argument is required! Trying running as './query.py inverted_index.txt'") 
    sys.exit()

fname = sys.argv[1]
with open(fname, "r") as f:
    lookup = eval(f.read())

def outputVals(word):
    try:
        doc_dict = lookup[word]
        print("\n'{}':".format(word))
    except:
        print("\n'{}': No results!".format(word))
        return 1

    for doc, lines in doc_dict.items():
        print("\t{}:".format(doc))
        for key, val in sorted(lines.items()):
            print("\t\tAppears {} times on line {}".format(val['count'], key))

    return 0

def parseInput(args):
    words = [x.strip().lower() for x in args.split(',')]
    words = list(set(filter(None, words)))
    for word in words:
        outputVals(word)
    print("")

'''
    try:
        words = [x.strip() for x in args.split(',')]
        outputVals(words)
    except:
        print("Bad input! Either the word does not exist or your input format is not supported.")
        return 1
'''


print("Starting the Inverted Index Querier, search for a single word or multiple words!")
print("Either enter a single word (i.e. hamlet) or multiple words separated by commas (i.e. hamlet, broken, today)")
print("Escape character is q or Q")
while True:
    words = input("> ")
    if words == 'q' or words == 'Q':
        break
    else:
        parseInput(words)

