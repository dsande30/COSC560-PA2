#!/usr/bin/env python
import sys
import os
import re
import json
import pprint

'''
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
'''

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

print(json.dumps(ii))
# with open('ii-results.json', 'w') as f:
# json.dump(ii, f)
