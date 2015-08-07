#/usr/bin/env python

import json
import jsonschema

def loadjson(filename):
    with open(filename) as file:
        return json.load(file)

schema = loadjson('schema/covschema.json')

doc = loadjson('testdata/valid/Coverage-Grid-standalone.covjson')

jsonschema.validate(doc, schema)
