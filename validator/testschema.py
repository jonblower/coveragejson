#/usr/bin/env python

import json
import jsonschema

def loadjson(filename):
    with open(filename) as file:
        return json.load(file)

schema = loadjson('schema/master.json')

doc = loadjson('testdata/valid/Coverage-Grid-standalone.covjson')
#doc = loadjson('testdata/valid/Range.covjson')
#doc = loadjson('testdata/valid/CoverageCollection-Point-param_in_collection-standalone.covjson')
#doc = loadjson('testdata/valid/CoverageCollection-empty-standalone.covjson')

jsonschema.validate(doc, schema)
