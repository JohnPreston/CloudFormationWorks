#!/usr/bin/env python

import os, sys
import json, yaml

if len(sys.argv) < 2:
    print "Input file missing"
    exit

with open(sys.argv[1], 'r') as fd:
    yaml_txt = fd.read()

yaml_dic = yaml.load(yaml_txt)

with open('converted.json', 'w') as fd:
    fd.write(json.dumps(yaml_dic))

print "File converted.yml successfully created"
