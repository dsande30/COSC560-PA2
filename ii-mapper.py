#!/usr/bin/env python
import sys
import os
import re

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        with open(root + os.path.sep + fname, 'r') as f:
            doc_id = fname
            i = 0
            for line in f.readlines():
                line = line.strip().lower()
                res = re.sub(ur"[^\w'\s]+",'', line)
                words = res.split()
                for word in words:
                    print("{}\t{}\t{}".format(doc_id, word, i))
                i += 1
