# CoverageJSON schemas

These schemas can validate many of the rules of the CoverageJSON specification. Example of use (Python):
```py
import json
import jsonschema # pip install jsonschema

def loadjson(filename):
    with open(filename) as file:
        return json.load(file)

schema = loadjson('schema/master.json')
doc = loadjson('testdata/valid/Coverage-Grid-standalone.covjson')

jsonschema.validate(doc, schema)
```

**TODO:** indicate in the spec somehow which rules can be validated by JSON schema?

**TODO:** The schemas are broken up into multiple files for maintainability purposes. This means that the schemas reference each other using `"$ref"` properties, e.g.:
```js
"properties": {
  "thing" : { "$ref": "file:./schema/thing.json" }
}
```
In this case the definition of the `thing` object is given in a separate schema document. The problem is that the path to the child schema is resolved relative to the *working directory of the validation code*, not the location of the parent schema. Therefore the child schema will only be resolved correctly when run from the correct directory; this is not portable. (Also it seems to cause problems when schemas references are more than one deep, i.e. a schema has a "grandchild".) We should use absolute URLs here when the schemas are published properly.

For developers: Here is a useful reference for understanding JSON schema: http://spacetelescope.github.io/understanding-json-schema/index.html. Note that we use constructs that only appear in Draft 4 of the JSON schema spec.
