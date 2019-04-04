#!/usr/bin/env python
import sys
import os
import re
import json
import pprint

ii = {}
for line in sys.stdin:
    doc_id, word, line_no = line.strip().split('\t')
    line_no = int(line_no)
    if word in ii:
        if doc_id in ii[word]:
            if line_no in ii[word][doc_id]:
                ii[word][doc_id][line_no]['count'] += 1
            else:
                ii[word][doc_id][line_no] = {}
                ii[word][doc_id][line_no]['count'] = 1
        else:
            ii[word][doc_id] = {}
            ii[word][doc_id][line_no] = {}
            ii[word][doc_id][line_no]['count'] = 1


    else:
        ii[word] = {}
        ii[word][doc_id] = {}
        ii[word][doc_id][line_no] = {}
        ii[word][doc_id][line_no]['count'] = 1

print(ii)
