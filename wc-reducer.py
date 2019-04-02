#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

wc = {}
threshold = 0.30

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if word in wc:
        wc[word] += count
    else:
        wc[word] = count

total = float(sum(wc.values()))
total_perc = 0
stops = {}
for key, val in sorted(wc.items(), key = itemgetter(1), reverse = True):
    perc = val/total
    total_perc += perc
    if total_perc < threshold:
        stops[key] = (val, perc)

    print ("{}\t{}\t{}".format(key, val, perc))

with open('stop_words.txt', 'w') as f:
    for key, val in sorted(stops.items(), key = itemgetter(1), reverse = True):
        f.write("{}\tCount: {}\t\tPercentage: {:.3}%\n".format(key, val[0], val[1]*100))
