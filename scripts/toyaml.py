#!/usr/bin/env python

import os, sys
import json, yaml

if len(sys.argv) < 2:
    print "Input file missing"
    exit

with open(sys.argv[1], 'r') as fd:
    json_txt = fd.read()

json_txt.strip()
json_dic = json.loads(json_txt)

with open('converted.yml', 'w') as fd:
    fd.write(yaml.safe_dump(json_dic,  allow_unicode=False))

print "File converted.yml successfully created"
