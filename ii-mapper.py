#!/usr/bin/env python
import sys
import os
import re

stop_words = []

with open(sys.argv[2]) as f:
    for line in f.readlines():
        word, count, freq = line.strip().split('\t')
        stop_words.append(word)

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        if '.crc' not in fname:
            with open(root + os.path.sep + fname, 'r') as f:
                doc_id = fname
                i = 0
                for line in f.readlines():
                    line = line.strip().lower()
                    res = re.sub(ur"[^\(a-zA-Z)'\s]+",'', line)
                    words = res.split()
                    for word in words:
                        if word not in stop_words:
                            print("{}\t{}\t{}".format(doc_id, word, i))
                    i += 1
