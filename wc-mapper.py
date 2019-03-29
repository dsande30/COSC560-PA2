#!/usr/bin/env python
"""mapper.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip().lower()
    res = re.sub(ur"[^\w'\s]+",'', line)
    words = res.split()
    for word in words:
        print("{}\t{}".format(word, 1))
