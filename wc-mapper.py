#!/usr/bin/env python
"""mapper.py"""

import sys
import re
import os

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        if '.crc' not in fname:
            with open(root + os.path.sep + fname, 'r') as f:
                for line in f.readlines():
                    line = line.strip().lower()
                    res = re.sub(ur"[^a-zA-Z'\s]+",'', line)
                    words = res.split()
                    for word in words:
                        print("{}\t{}".format(word, 1))
