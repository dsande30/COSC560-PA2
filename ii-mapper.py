#!/usr/bin/env python
import sys
import os
import re

# print("About to walk this ho")
for root, dirs, files in os.walk('shakebooks'):
    for fname in files:
        if '.crc' not in fname:
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
